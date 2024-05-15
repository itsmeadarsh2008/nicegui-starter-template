import os
from nicegui import ui

def loadStatic(ui, path, directory='static', file_types=['.css', '.scss', '.sass']):
    """
    Loads static content from either a local file or a CDN URL.

    :param ui: An object that has methods to add CSS, SCSS, and SASS content.
    :param path: The path to the local file or the URL of the CDN.
    :param directory: The directory to search for CSS, SCSS, and SASS files.
    :param file_types: The file types to search for.
    """
    print('Loading Static Files')
    # Check if the path is a local file or a URL
    if os.path.isfile(path):
        # Read the content of the local file
        with open(path, 'r') as file:
            content = file.read()
        
        # Determine the type of file and execute the appropriate method
        if path.endswith('.scss'):
            ui.add_scss(content)
        elif path.endswith('.sass'):
            ui.add_sass(content)
        elif path.endswith('.css'):
            ui.add_css(content)
    else:
        # Generate an import statement for the CDN URL
        if any(path.endswith(ft) for ft in file_types):
            # Determine the type of file and generate the appropriate import statement
            if path.endswith('.scss'):
                ui.add_scss(f'@import url(\"{path}\");')
            elif path.endswith('.sass'):
                ui.add_sass(f'@import url(\"{path}\");')
            elif path.endswith('.css'):
                ui.add_css(f'@import url(\"{path}\");')
            