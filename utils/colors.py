import random
import time

bootstrap_colors = ['primary', 'secondary', 'info', 'success', 'warning', 'danger']
black_white_colors = ['black', 'gray-dark', 'gray', 'light']
adminlte_colors = ['indigo', 'lightblue', 'navy', 'purple', 'fuchsia', 'pink', 'maroon', 'orange', 'lime', 'teal',
                   'olive']


def random_color_bootstrap(seed: int = None):
    rnd = random.Random(seed * time.time())
    item = bootstrap_colors[rnd.randint(0, len(bootstrap_colors) - 1)]
    return item


def random_color(seed: int = None):
    rnd = random.Random(seed * time.time())
    colors = bootstrap_colors + adminlte_colors
    item = colors[rnd.randint(0, len(colors) - 1)]
    return item


def random_bg(seed: int = None):
    return f'bg-{random_color(seed)}'


def random_text(seed: int = None):
    return f'text-{random_color(seed)}'
