from flask import Blueprint, request, jsonify
import httpx
from Utils.Auth.hpi_auth import authenticate

Patient = Blueprint('Patient', __name__)

@Patient.route('/Patient')
def patient():
    appName = request.args.get('appName')
    patientId = request.args.get('NHI')
    userId = request.args.get('userId')

    if not appName:
        return 'Error: appName variable is missing', 400
    if not patientId:
        return 'Error: patientId / NHI is missing', 400
    if not userId:
        return 'Error: userId not provided', 400
    
    access_token = authenticate(application=appName)
    api_key = 'KSLSzh5s9P25wL5O1qZ8w90zrbraocFX8XTBL6F9'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'x-api-key': api_key,
        'userId': userId
    }

    url_base = 'https://api.hip-uat.digital.health.nz/fhir/nhi/v1'
    endpoint = '/Patient'
    url = url_base + endpoint + '/' + patientId

    print(f'URL to Call: {url}')

    try:
        response = httpx.get(url, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except httpx.HTTPError as e:
        print(f'HTTP Error has occurred - {e}')
        return jsonify({'error': 'Failed to fetch data from API'}), 500