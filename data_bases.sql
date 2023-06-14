#Create the new Schema where all the data base will be archived (I´ll use utf8 to record possible responses in Spanish):
CREATE SCHEMA `us_project` DEFAULT CHARACTER SET utf8 ;

# 1)Here I create the User table:
#Here I can save all the information about the user.
CREATE TABLE `us_project`.`user` (
  `user_id` INT NOT NULL,
  `name` VARCHAR(20) NOT NULL,
  `last_name` VARCHAR(20) NOT NULL,
  `city` VARCHAR(20) NOT NULL,
  `email` VARCHAR(40) CHARACTER SET 'utf8' NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE);

# 2)Now, the table Orders:
#I can save here the information about the orders that a user can make:
CREATE TABLE `us_project`.`orders` (
  `orders_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `date` TIMESTAMP NOT NULL,
  `product_id` INT NOT NULL,
  `type_product_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  PRIMARY KEY (`orders_id`));


# 3) Now, the table Product:
#Here I´ll save the differents products that can be storaged into the warehouse:
CREATE TABLE `us_project`.`product` (
  `product_id` INT NOT NULL,
  `name` VARCHAR(20) CHARACTER SET 'utf8' NOT NULL,
  PRIMARY KEY (`product_id`));
  
# 4) Now, the table Type_product:
#I can save here the different kind of products that can be storaged into the warehouse:
CREATE TABLE `us_project`.`type_product` (
  `type_product_id` INT NOT NULL,
  `type` VARCHAR(20) CHARACTER SET 'utf8' NOT NULL,
  PRIMARY KEY (`type_product_id`));


#Now, I need to stablished the relations betewen the keys in my tables:
ALTER TABLE `us_project`.`orders` 
ADD INDEX `orders_user_idx` (`user_id` ASC) VISIBLE,
ADD INDEX `orders_product_idx` (`product_id` ASC) VISIBLE,
ADD INDEX `orders_type_product_idx` (`type_product_id` ASC) VISIBLE;
;
ALTER TABLE `us_project`.`orders` 
ADD CONSTRAINT `orders_user`
  FOREIGN KEY (`user_id`)
  REFERENCES `us_project`.`user` (`user_id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
ADD CONSTRAINT `orders_product`
  FOREIGN KEY (`product_id`)
  REFERENCES `us_project`.`product` (`product_id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
ADD CONSTRAINT `orders_type_product`
  FOREIGN KEY (`type_product_id`)
  REFERENCES `us_project`.`type_product` (`type_product_id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;


#You can check in .idea/Reverse_engineer_orders.jpg the graphical representation of the currently created databases.

