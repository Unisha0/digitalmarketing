from .reels import REELS, HOME_REELS


def reels(request):
    """Make the work reels available to every template as `reels`."""
    return {'reels': REELS, 'home_reels': HOME_REELS}
