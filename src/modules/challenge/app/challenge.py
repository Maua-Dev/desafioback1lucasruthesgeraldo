import base64
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import boto3
from src.shared.helpers.functions.compose_cartoon_email import compose_cartoon_email
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpResponse


def lambda_handler(event, context):
    
    s3 = boto3.client('s3', 'sa-east-1')

    s3_bucket_name = 'challenge-storage-devcommunitymaua'
    s3_object_key = 'kick buttowski.png'
    
    img = s3.get_object(Bucket = s3_bucket_name, Key = s3_object_key)
    
    img_read = img['Body'].read() 
    
    mime_base = MIMEBase('image', 'png')
    mime_base.set_payload(img_read)
    encoders.encode_base64(mime_base)
    mime_base.add_header('Content-Disposition', f'attachment; filename="{s3_object_key}"')
    message = MIMEMultipart()
    message.attach(mime_base)

    charles_cartoon_composed_email_html = compose_cartoon_email(message.as_string())

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