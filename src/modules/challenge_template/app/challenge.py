import base64
import boto3
from src.modules.challenge_template.app import compose_cartoon_email
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


def lambda_handler(event, context):
    
    s3 = boto3.client('s3')

    img = s3.get_object('challenge-storage-devcommunitymaua ', Key='kick buttowski.png')
    
    img_read = img['Body'].read() 
    
    img_64 = base64.b64encode(img_read).decode('utf-8')

    charles_cartoon_composed_email_html = compose_cartoon_email(img_64)

    client_ses = boto3.client('ses', 'sa-east-1')

    response = client_ses.send_email(
                Destination={
                    'ToAddresses': [
                        "mateus.c.martins@outlook.com",
                    ],
                    'BccAddresses':
                        [
                            "lucascrapino@gmail.com"
                        ]
                },
                Message={
                    'Body': {       
                        'Html': {
                            'Charset': "UTF-8",
                            'Data': charles_cartoon_composed_email_html,
                        },
                    },
                    'Subject': {
                        'Charset': "UTF-8",
                        'Data': "Charles - Envio de desenho",
                    },
                },
                Source="devmaua@gmail.com",
            )
     
    return LambdaHttpResponse(statusCode=200, body=response)