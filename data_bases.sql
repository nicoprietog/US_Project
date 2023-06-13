#Create the new Schema where all the data base will be archived (I´ll use utf8 to record possible responses in Spanish):
CREATE SCHEMA `us_project` DEFAULT CHARACTER SET utf8 ;

#I´ll create the first table, the one that will register the Type of products:
CREATE TABLE `type_product`.`us_project` (
  `id_type` INT NOT NULL,
  `type_product` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id_type`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

#Add the Types of products:
INSERT INTO type_product(id_type,type_product)
VALUES ('1', 'coffee makers'),
       ('2', 'coffee pots'),
       ('3', 'spare parts');
