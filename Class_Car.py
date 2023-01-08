#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Car:
    '''
    Creates a car that can drive and keep track of mileage.
    
    Parameters
    ----------
    color: string
        Color of car
        
    price: int, float
        Price of car
        
    transmission: string
        Manual or Automatic
    
    mileage: int or float
        Initial mileage of car
        
    make: str
       Name of car manufacturer
       
    model: str
        Name of model
    '''
    
    def __init__(self, color, price, transmission, 
                 mileage, make, model):
        self.color = color
        self.price = price
        self.transmission = transmission
        self.mileage = mileage
        self.make = make
        self.model = model
        self.wheels = 4
        self.depreciation = .5
    
    def drive(self, miles):
        '''
        Drive the car and add the current miles to the total
        
        Parameters
        ----------
        miles: int or float
            The number of miles driven
        '''
        self.mileage += miles
        self.price -= miles * self.depreciation
        print(f'Your {self.make} {self.model} drove {miles} miles')
        print(f'Total miles driven: {self.mileage}')
        print(f'Current value of car: {self.price}')
        
    def future_lifetime(self):
        '''
        Calculate the future lifetime of the car in miles
        
        Returns
        -------
        The number of miles left as a float
        '''
        return self.price / self.depreciation


# ### Calling methods from attributes within your class
# 
# Our `Car` instances from above have several attributes. Each of these attributes is another object. For example, the `color` attribute is a string and the `mileage` attribute is an integer. Each of these objects have their own attributes and methods like everything else. Let's call the `upper` method of the `color` string attribute. Notice that this uses dot notation twice. First to access `color` and then to access its method `upper`.

# In[7]:


my_car = Car(color='Silver', price=35000, transmission='Manual', 
             mileage=0, make='Tesla', model='S3')

my_car.color.upper()


# ### Setting an attribute to an instance from a user-defined class
# 
# So far, the attributes of our car class have been quite simple, and limited to the built-in integer and string types. We can assign our attributes to user-defined types as well. Let's redefine the car class to also accept a driver during initialization. This driver will be a member of the Person class, which we define below.

# In[1]:


class Person:
    
    def __init__(self, first, last, sex, age, height):
        self.first = first
        self.last = last
        self.sex = sex
        self.age = age
        self.height = height
        
    def greet(self):
        return f'Hello, my name is {self.first} {self.last}'

class Car:
    
    def __init__(self, color, price, transmission, 
                 mileage, make, model, driver):
        self.color = color
        self.price = price
        self.transmission = transmission
        self.mileage = mileage
        self.make = make
        self.model = model
        self.driver = driver
        self.wheels = 4
        self.depreciation = .5
    
    def drive(self, miles):
        self.mileage += miles
        self.price -= miles * self.depreciation
        print(f'Your {self.make} {self.model} drove {miles} miles')
        print(f'Total miles driven: {self.mileage}')
        print(f'Current value of car: {self.price}')
        
    def future_lifetime(self):
        return self.price / self.depreciation


# Our Car constructor demands a person instance to be created first since it's now passed as an argument to its constructor. Let's begin by creating a Person instance.

# In[2]:


some_person = Person('LeBron', 'James', 'M', 37, 80)


# We now create a new Car instance passing in the Person instance as the last argument.

# In[3]:


my_car = Car(color='Silver', price=35000, transmission='Manual', 
             mileage=0, make='Tesla', model='S3', driver=some_person)


# Let's now call the greet method on the Person instance assigned to the driver attribute of the Car instance.

# In[4]:


my_car.driver.greet()


# Here, we have even more levels of dot notation.

# In[5]:


my_car.driver.first.upper()

