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
  `id` INT NOT NULL,
  `date` TIMESTAMP NOT NULL,
  `name` VARCHAR(20) NOT NULL,
  `last_name` VARCHAR(20) NOT NULL,
  `id_buyer` INT NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `city` VARCHAR(20) NOT NULL,
  `company_type` VARCHAR(20) CHARACTER SET 'armscii8' NOT NULL,
  `kind` INT NOT NULL,
  `type` INT NOT NULL,
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

# 5) This table save the status of the allocated orders: 
CREATE TABLE `us_project`.`to_allocate` (
  `id_allocate` INT NOT NULL AUTO_INCREMENT,
  `id_orders` INT NOT NULL,
  `allocated` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_allocate`),
  UNIQUE INDEX `id_allocate_UNIQUE` (`id_allocate` ASC) VISIBLE,
  INDEX `id_order_idx` (`id_orders` ASC) VISIBLE,
  CONSTRAINT `allocate_order`
    FOREIGN KEY (`id_orders`)
    REFERENCES `us_project`.`orders` (`id_orders`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

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
