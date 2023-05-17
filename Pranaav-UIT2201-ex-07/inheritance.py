# -*- coding: utf-8 -*-


"""

This module provides a series of classes that derive certain
functionalities from a parent class and overload some parent
class operations for each child class. This is a part of the exercises
given under the course UIT2201 (Programming and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 17 2023

Revised on Wed May 17 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

"""


class product:

    '''
    The Product class represents a product with its name, price,
    and quantity. It provides methods for performing various
    operations related to the product.

    The input data is not modified in any way and there are
    no side effects.
    
    Methods:
        __init__(self, name, price, quantity): Initializes a new instance
        of the Product class with the specified name, price, and quantity.

        __add__(self, other): Adds the quantities and prices of two products
        and displays a combo offer message.

        display_information(self): Displays the name, price, and quantity
        of the product.

        cost_calc(self): Calculates and displays the total cost of the
        product.

    '''

    def __init__(self,name,price,quantity):

        self.name = name
        self.price = price
        self.quantity = quantity

    def __add__(self,other):
        
        prods = [self.name, other.name]
        total_cost = (self.price * self.quantity) + (other.price * other.quantity)
        print(f"Combo offer for {self.name} and {other.name} !\n For a price of {total_cost}")
    
    def display_information(self):

        print("Name is : ",self.name)
        print("Price is : ",self.price)
        print("Quantity is : ",self.quantity)

    def cost_calc(self):

        print("Total cost is : ", self.price * self.quantity)


class ElectronicProduct(product):

    '''
    The ElectronicProduct class represents an electronic product,
    which is a specialized type of Product. It inherits the attributes
    and methods from the Product class and adds additional attributes
    for brand and model.
    
    The ElectronicProduct class extends the functionality of the
    Product class and includes additional attributes for brand and
    model.

    It inherits the methods from the Product class, including
    display_information(), which is overridden to also display
    the brand and model.

    The ElectronicProduct class does not modify the input data
    and has no side effects.

    Methods:
        __init__(self, name, price, quantity, brand, model): Initializes a new
        instance of the ElectronicProduct class with the specified name,
        price, quantity, brand, and model.

        display_information(self): Displays the name, price, quantity, brand,
        and model of the electronic product.

    '''

    def __init__(self, name, price, quantity, brand, model):

        super().__init__(name, price, quantity)
        self.brand = brand
        self.model = model

    def display_information(self):

        super().display_information()
        print("Brand is : ",self.brand)
        print("Model is : ",self.model)


class ClothingProduct(product):

    '''
    The ClothingProduct class represents a clothing product,
    which is a specialized type of Product. It inherits the attributes
    and methods from the Product class and adds additional attributes
    for size and color.
    
    The ClothingProduct class extends the functionality of the
    Product class and includes additional attributes for size and
    color.

    It inherits the methods from the Product class, including
    display_information(), which is overridden to also display
    the size and color.

    The ClothingProduct class does not modify the input data
    and has no side effects.

    Methods:
        __init__(self, name, price, quantity, size, color): Initializes a new
        instance of the ClothingProduct class with the specified name,
        price, quantity, size, and color.

        display_information(self):
            Displays the name, price, quantity, size, and color of the clothing
            product.
    
    '''

    def __init__(self, name, price, quantity, size, color):

        super().__init__(name, price, quantity)
        self.size = size
        self.color = color

    def display_information(self):

        super().display_information()
        print("Size is : ",self.size)
        print("Color is : ",self.color)


def add_items_clothing(data_dict,size,color):

    '''
    The add_items_clothing function takes a dictionary containing data
    of clothing products, as well as lists for sizes and colors. It
    creates ClothingProduct objects based on the data and returns a
    list of these objects.

    The input is not modified in any way and there are no side effects.

    Parameters:
        data_dict: A dictionary containing the data of clothing products.
        The keys are the names of the products, and the values are lists of
        [price, quantity].
        size: A list of sizes corresponding to each product in the data_dict.
        color: A list of colors corresponding to each product in the data_dict.

    Returns:
        A list of ClothingProduct objects created based on the data provided.

    '''

    keys = [x for x in data_dict.keys()]
    clothing_objects = []

    for key in range(len(keys)):
        name = keys[key]
        price, quantity = data_dict[name]
        clothing_objects.append(ClothingProduct(name,price,quantity,size[key],color[key]))

    return clothing_objects


def add_items_electronic(data_dict,brand,model):

    '''
    The add_items_electronic function takes a dictionary containing data of
    electronic products, as well as lists for brands and models. It creates
    ElectronicProduct objects based on the data and returns a list of these
    objects.

    Parameters:
        data_dict: A dictionary containing the data of electronic products.
        The keys are the names of the products, and the values are lists of
        [price, quantity].
        brand: A list of brands corresponding to each product in the data_dict.
        model: A list of models corresponding to each product in the data_dict.

    Returns:
        A list of ElectronicProduct objects created based on the data provided.
    
    '''

    keys = [x for x in data_dict.keys()]
    Electronic_objects = []
    
    for key in range(len(keys)):
        name = keys[key]
        price, quantity = data_dict[name]
        Electronic_objects.append(ElectronicProduct(name,price,quantity,brand[key],model[key]))

    return Electronic_objects


def input_create(data_dict):

    '''
    The input_create function prompts the user to enter information
    for a new product and adds it to the provided data_dict.

    Parameters:
        data_dict: A dictionary containing the existing data of
        products.

    Returns:
        The updated data_dict with the newly added product.

    '''

    name = input("Enter name : ")
    price = int(input("Enter price : "))
    quantity = int(input("Enter quantity : "))
    vals = [price,quantity]
    data_dict[name] = vals

    return data_dict


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    a = ElectronicProduct("Ra",500,5,"louis","EX1550")
    b = ClothingProduct("OANR",10000,1,"louis vitton","MANN0912")
    c = ClothingProduct("ajlskfd",15000,2,"louis vitton","MANN12")

    a.display_information()
    print()
    b.display_information()
    print()

    b+c

    data_dict = {}
    brand_names = []
    model_names = []

    n = int(input("Enter number of entries : "))

    for i in range(n):
        data_dict = input_create(data_dict)
        brand = input("Enter brand name : ")
        model = input("Enter model name : ")
        brand_names.append(brand)
        model_names.append(model)
    
    electronic_objects = add_items_electronic(data_dict,brand_names,model_names)

    data_dict = {}
    sizes = []
    colors = []

    n = int(input("Enter number of entries : "))

    for i in range(n):
        data_dict = input_create(data_dict)
        size = input("Enter size : ")
        color = input("Enter color name : ")
        sizes.append(size)
        colors.append(color)

    clothing_objects = add_items_clothing(data_dict,sizes,colors)

    for electronic_object in electronic_objects:
        electronic_object.display_information()
        print()

    for Clothing_object in clothing_objects:
        Clothing_object.display_information()
        print()

