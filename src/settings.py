from mode import Mode



class Settings():
    """Stores the ui settings.
    
    Attributes:
        mode (mode.Mode) : the color scheme of the ui
    """

    mode = None

    def __init__(self):
        """ Initializes this settings object with default settings if `from_string` is not set.
        
        Args:
            from_string : string representaiton of a settings object which should be used for initialization
        """
        
        self.mode = Mode.DARK

    def __str__(self):
        string = "mode = " + self._mode

        return string
