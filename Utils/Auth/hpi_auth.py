import httpx

def authenticate(application):
    """
    Function to determine which application the request is coming from and send the appropriate credentials to the get_auth_token function.

    Args:
    - application: Nmae (or short name) of the application the request is coming from.
    """
    hpi_auth_url = 'https://hpi-hip-uat.auth.ap-southeast-2.amazoncognito.com/oauth2/token'
    if application == 'RCP':
        print('Source = RCP')
        try:
            client_id = '2h9emq7d1aeoaqdigbikeljkbq'
            client_secret = '3tmrgqd0e04c3haddspbcri5elkqhnqaomb1lusdfdccvl4qveo'
            print('Requesting OAuth Token with RCP Credentials')
            auth_token = get_auth_token(client_id, client_secret, hpi_auth_url)
            return auth_token
        except:
            print('Error occured.')
            return None
        
def get_auth_token(client_id, client_secret, token_url):
    """
    Function to obtain an access token from an OAuth 2.0 API using client credentials

    Args:
    - client_id: The client ID provided by the OAuth provider
    - client_secret: The client secret provided by the OAuth provider
    - token_url: The URL to request an auth token from

    Returns:
    - Auth token if successful, None otherwise.
    """
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    try:
        print('Sending request for OAuth Token')
        response = httpx.post(token_url, data=data)
        response.raise_for_status()
        token_data = response.json()
        access_token = token_data.get('access_token')
        print('Auth token received')
        return access_token
    except httpx.HTTPError as e:
        print(f'HTTP error occurred: {e}')
        return None