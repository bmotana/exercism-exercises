class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.
    
    Attributes:
        message: Explanation of the error.
    """
    def __init__(self, message: str):
        """Initialize the exception with a message.
        
        Args:
            message: Description of the error condition.
        """
        self.message = message
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.
    
    Attributes:
        message: Explanation of the error.
    """
    def __init__(self, message: str):
        """Initialize the exception with a message.
        
        Args:
            message: Description of the error condition.
        """
        self.message = message
        super().__init__(message)


class CircularBuffer:
    """A fixed-size buffer that overwrites oldest data when full.
    
    A circular buffer optimized for storing and retrieving data in a FIFO manner,
    with a fixed capacity. When the buffer reaches its capacity, new writes will
    fail unless using the overwrite method.
    """
    
    def __init__(self, capacity: int):
        """Initialize a new CircularBuffer with the specified capacity.
        
        Args:
            capacity: Maximum number of elements the buffer can hold.
        
        Raises:
            ValueError: If capacity is not a positive integer.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
            
        self.capacity = capacity
        self.buffer = []  # Using a list to store buffer elements
        self.has_data = False  # Flag to track if buffer has ever had data
    
    def read(self) -> str:
        """Read and remove the oldest item from the buffer.
        
        Returns:
            The oldest item in the buffer.
        
        Raises:
            BufferEmptyException: If the buffer is empty.
        """
        if not self.has_data or not self.buffer:
            raise BufferEmptyException("Circular buffer is empty")
            
        # Remove and return the oldest item (first element)
        return self.buffer.pop(0)
        
    def write(self, data: str) -> None:
        """Write an item to the buffer if it's not full.
        
        Args:
            data: The data to be written to the buffer.
            
        Returns:
            None
            
        Raises:
            BufferFullException: If the buffer is at capacity.
        """
        if len(self.buffer) >= self.capacity:
            raise BufferFullException("Circular buffer is full")
            
        self.buffer.append(data)
        self.has_data = True  # Mark that the buffer has data
    
    def overwrite(self, data: str) -> None:
        """Write an item to the buffer, overwriting oldest item if buffer is full.
        
        If the buffer is not full, this behaves like the write method.
        If the buffer is full, the oldest item is removed before adding the new item.
        
        Args:
            data: The data to be written to the buffer.
            
        Returns:
            None
        """
        if len(self.buffer) >= self.capacity:
            # Remove the oldest item (first element) to make room
            self.buffer.pop(0)
            
        self.buffer.append(data)
        self.has_data = True  # Mark that the buffer has data
        
    def clear(self) -> None:
        """Clear all items from the buffer but maintain its capacity.
        
        Returns:
            None
        """
        self.buffer = []
        # Note: We don't reset has_data to False since the buffer has had data historically
    
    def is_empty(self) -> bool:
        """Check if the buffer is currently empty.
        
        Returns:
            True if the buffer contains no items, False otherwise.
        """
        return len(self.buffer) == 0
    
    def is_full(self) -> bool:
        """Check if the buffer is currently full.
        
        Returns:
            True if the buffer has reached capacity, False otherwise.
        """
        return len(self.buffer) >= self.capacity
    
    def __len__(self) -> int:
        """Return the current number of items in the buffer.
        
        Returns:
            Integer representing the current buffer size.
        """
        return len(self.buffer)


