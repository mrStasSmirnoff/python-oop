## Class vs Instance methods
### Instance Methods
- Definition: Instance methods are functions that are defined inside a class and can only be called from an instance of that class.
- Access to: They have access to the instance (self) and through it, they can modify the object's state and access its instance attributes.
Example: In your code, calc_total_price and apply_discount are instance methods. They operate on a specific instance of Item, modifying or using the attributes (self.name, self.price, self.quantity) of that instance.

### Class Methods
- Definition: Class methods are methods that are bound to the class rather than its objects. They can modify the class state that applies across all instances of the class.
- Access to: They take a cls parameter that points to the class—and not the object instance—when the method is called.
- Use Case: Class methods are often used for factory methods, which instantiate an instance of a class, using different parameters than those usually passed to the class constructor.

#### Why instantiate_from_csv as a Class Method?
- Purpose: If instantiate_from_csv is meant to read a CSV file and create multiple Item instances from it, it aligns more with the behavior of a class method.
- Reasoning: This method would be operating on a class level, creating new instances of the Item class based on the data read from a CSV file. It's not modifying or interacting with a specific instance but is instead used to create new instances.
- Converting to a Class Method
To convert instantiate_from_csv to a class method, you'd use the @classmethod decorator.
