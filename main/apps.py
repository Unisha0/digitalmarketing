from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


from django.contrib.staticfiles.apps import StaticFilesConfig as _StaticFilesConfig


class StaticFilesConfig(_StaticFilesConfig):
    # tailwind-input.css is build tooling (contains @import "tailwindcss"); it must not be
    # collected or hashed - only the compiled tailwind-built.css is served.
    ignore_patterns = _StaticFilesConfig.ignore_patterns + ['tailwind-input.css']
