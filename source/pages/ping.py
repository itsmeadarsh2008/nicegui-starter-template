from nicegui import ui
import http.client
import urllib.parse

def create_status_checker(ui: ui, site_to_check='https://example.com'):
    # Create a NiceGUI page
    # Text to display the status
    status_text = ui.label('Click the button to check the status.').classes('text-xl')

    # Button to trigger the status check
    def check_status():
        try:
            # Parse the URL to get the hostname and path
            parsed_url = urllib.parse.urlparse(site_to_check)
            hostname = parsed_url.hostname
            path = parsed_url.path if parsed_url.path else '/'

            # Create a connection
            conn = http.client.HTTPSConnection(hostname)

            # Perform the request and get the status code
            conn.request("GET", path)
            response = conn.getresponse()
            status_code = response.status

            # Update the status text
            ui.notify(f'Status code: {status_code}',type='positive')

            # Close the connection
            conn.close()
        except Exception as e:
            # Handle exceptions
            status_text.set_text(f'Error: {e}',type='negative')

    # Add the button to the UI
    ui.button('Ping', color='primary', on_click=check_status).props('push')