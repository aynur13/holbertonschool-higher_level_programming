class Square:
    """Represent a square."""
    
    def __init__(self, size=0):
        """Initialize a new Square."""
        if not isinstance(size, int) or size < 0:
            raise TypeError("size must be an integer") if not isinstance(size, int) else ValueError("size must be >= 0")
        self.__size = size
