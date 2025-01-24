def compose_cartoon_email(img_base64:str):
    message = """
    
<!DOCTYPE html>
        <html lang="pt-br" charset="UTF-8">
        <head>
        </head>
        <body style="margin: 0; padding: 0; display: flex; align-items: center; justify-content: center; min-height: 100vh; background-color: white; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
        <table class="main" style="width: 50vw; max-width: 600px; background-color: white; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.25); overflow: hidden;">
            <tr>
            <td>
                <table class="TittleBox" style="width: 100%; background-color: #110e47; border-radius: 10px 10px 0 0;">
                <tr>
                    <td style="text-align: center; padding: 20px;">
                    <img alt="Logo Dev" src="https://media.licdn.com/dms/image/v2/D4D0BAQGs_HkPBVnYEQ/company-logo_200_200/company-logo_200_200/0/1683726981796?e=2147483647&v=beta&t=Hq5PGRi2XRJ72o5Cqhy2NI75y4xt4SeddISbnwQ7SUY" style="width: 60%;"/>
                    <h1 style="color: #ffffff; margin-top: 10px;"><strong>Desenho encontrado!</strong></h1>
                    <img alt="Desenho" src="{img_base64}" style="width: 100%;"/>
                    </td>
                </tr>
                </table>
                <table class="ContentBox" style="width: 100%; background-color: #282470; border-top: 1px solid #ffffff; border-radius: 0 0 10px 10px;">
                <tr>
                    <td style="text-align: center; padding: 20px;">
                    <div class="TextsBox" style="word-wrap: break-word;">
                        <h2 style="color: #ffffff;">Olá, Charles. Encotramos a imagem do desenho que você gostava de assistir!</p></h2>
                    </div>
                    </td>
                </tr>
                </table>
                <table class="BottomBox" style="width: 100%; background-color: #110e47; border-top: 1px solid #ffffff; border-radius: 0 0 10px 10px;">
                <tr>
                    <td style="text-align: center; padding: 20px;">
                    <div class="TextsBox" style="color: #ffffff; word-wrap: break-word;">
                        <h2>Atenciosamente,</h2>
                        <h2><strong>Dev Community Mauá. #EhOBeckas😎</strong>&#127744;</h2>
                    </div>
                    </td>
                </tr>
                </table>
            </td>
            </tr>
        </table>
        </body>
        </html>


"""

    message = message.format(img_base64 = img_base64)

    return message