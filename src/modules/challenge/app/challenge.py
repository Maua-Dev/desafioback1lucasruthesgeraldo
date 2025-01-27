import base64
import boto3
from src.shared.helpers.functions.compose_cartoon_email import compose_cartoon_email
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpResponse


def lambda_handler(event, context):
    
    s3 = boto3.client('s3', 'sa-east-1')

    s3_bucket_name = 'challenge-storage-devcommunitymaua'
    s3_object_key = 'kick buttowski.png'
    
    img = s3.get_object(Bucket = s3_bucket_name, Key = s3_object_key)
    
    img_read = img['Body'].read() 
    
    img_64 = base64.b64encode(img_read).decode('utf-8')

    charles_cartoon_composed_email_html = compose_cartoon_email(img_64)

    client_ses = boto3.client('ses', 'sa-east-1')

    response = client_ses.send_email(
                Destination={
                    'ToAddresses': [
                        "mateus.c.martins@outlook.com",
                        "22.00667-2@maua.br"
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
                Source="contato@devmaua.com",
            )
     
    return LambdaHttpResponse(status_code=200, body=response)