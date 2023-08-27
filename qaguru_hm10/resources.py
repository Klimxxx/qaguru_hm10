import os


def resource_path(image):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, f'resources/{image}'))
