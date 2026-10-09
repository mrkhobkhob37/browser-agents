"""Python 3 compatibility helpers (Python 2 support removed in fork)."""
import sys  # noqa: F401

string_types = str


def iteritems(d, **kw):
    return iter(d.items(**kw))
