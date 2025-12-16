from enum import Enum

class RefreshPolicy(Enum):
    """
    Enum to define the allowed values for the 'refresh' parameter
    across ElasticsearchDocumentStore methods.
    """
    FALSE = False       # Default: No immediate refresh.
    TRUE = True         # Force immediate refresh.
    WAIT_FOR = "wait_for" # Wait for the next refresh cycle.