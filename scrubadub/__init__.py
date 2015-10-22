
# convenient imports
from .scrubbers import Scrubber


__version__ = VERSION = "0.1.0"


def clean(text, cls=None, **kwargs):
    """Public facing function to clean ``text`` using the scrubber ``cls`` by
    replacing all personal information with ``{{PLACEHOLDERS}}``.
    """
    cls = cls or Scrubber
    scrubber = cls()
    return scrubber.clean(text, **kwargs)
