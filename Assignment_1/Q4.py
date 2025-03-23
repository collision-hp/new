'''In Python, access control to class attributes and methods is implemented using naming conventions rather than strict enforcement.'''

''' Public: Fully accessible from anywhere. no naming convetion.
 Protected: Intended for internal or subclass use, but still accessible from outside by convention. A single leading underscore (e.g., self._attribute).
 
 Private: Harder to access due to name mangling, but can still be accessed using the mangled name (intended for internal class use only).
 Naming Convention: Two leading underscores (e.g., self.__attribute).'''