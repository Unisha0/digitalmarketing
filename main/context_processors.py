from .reels import REELS


def reels(request):
    """Make the work reels available to every template as `reels`."""
    return {'reels': REELS}
