from firebase_admin import credentials, messaging, initialize_app

file = {
    "type": "service_account",
    "project_id": "clinic-template-f3470",
    "private_key_id": "595dd2d01a275ab9e4b8edb304c70b349fa57d99",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCtguVjjrSxzy4z\n/wlEtnOkFPlKE0zbw2F6ALAaR8H9LreBWIfCtDp99xZaJd+fM78CIaQUnAyuPPLZ\nL0Cc1v1VFOOsabthd1DmQFrhSW6Oo1ZYMHi7KArVoKVu0ya9rb3stJBmYZRfVUQn\nqMQYXBNytgAAyfTVDGrQyWOPrrXShMVk7i7yq8FWHCR33duFy809fr/zI9hxED6s\nqIQrlJy/vFKPzSqWqAoKXg2sJCOyLO0hXHKYzSTkypEfX6CyjZ4wP2aGs+UBhXco\nT06POpkfwcmOZ6TX5EKujcQDGSrAld4lCjlussiu6aSqMF2+EwSIOjS9D1vC10go\nv4BsZcGvAgMBAAECggEAEyVH6YHkJ2CckQk5vRbC0N6tmUJi7zbyaRNtWyEC40yF\n3CRoKpBXifG7Siw2rir4DySmJc4ISiuYgmWH5CaG4p4A91PdZMZVK2r7fDNtmxij\n3OxQThp/g44L4xwygKiMtfNAocNvq0tNz3B8XtG+JaC2hF/Ef8O0f6BRN5gIIRft\nkWZqnWPZNBFPOgpZy+e93TWnEK9Dd0jZGz2Ti8hC0VaqJzsE4CmrQR+vLTxQaR4N\nTo6GTTuD6x8r0+YDx5hrmrBMBLekaU6BRqgS+gsO92GBnIhd9/s/iNol4/ElwAgB\nh80UvzNkHiUS/aOUrVd5B7Kk1/E/Wcze6TIBc9rXiQKBgQDuQpxI3nGBT2fzDD2c\nyXRmZV3xJ3p8q6VuzA4b3MfhS0mTmnIUNC4wSve2akIjOhOdePom2ECBYH4bQrGz\nrnarfkxV7lxLRS3alo12zJlEpq4BMiXQ2ktp0cP42PWZ1dcGK8UkA2WDPfPHkELT\nwxtzYMNctnwnoi0javouxcZTVwKBgQC6biGKeAqCTJogsuuQ1qkUSqYU5Qg+onu8\nxoqydaQfxuEbmw9us/L1j+38UNuNwXNNZ+zgep8u8ACHGYViwTXvKzxWPtNtc4an\n+vkrWtWLrrXUXB3Fv0jApRQt9vdF5YhTDQ4NNsMpdKuxx+/4buYi/7iHQYgYWqSh\nmN5XjM4laQKBgQDKMTzvmdY5JmnQmFKw+0UMoHlYbWhE5GU/4WsXugTl7D5ERI0L\nGD0aPoR5CTOXMXHz8PZYgKw9HuXlvHORSDzszAF76wvn1I1VMu5aIsbuu4Ru/1+Y\nHahh5OGqDHRgWFhhpENojHlZJvn6ITKVAr4I69TemP5DpB0qMV6e0re7gQKBgETd\nCWaskLUwtn39mSYXJL1qFY8CStlYC3zfmbvx2H4kaGJaFIk/zy8Fy1K4S2FBY+Xj\nzYvdv48G+CrvMmYYGGQQBGmXK2HymnrSKdfp5ZeDIYcfv5+b2LPQRnP0FcKr1n9X\nAym+YLifcAxrXijWTgv/iZnsiuj0Envei8KrMDqBAoGAeJm9p7QSkfDlxkYt47PV\nr1tRf6QdktpFIua4whM1dZRgm/VdmgkZ2uMuyl9gOV7G4RavGvw3POultJOcF8db\noLNi3nPEM+T/xbM9oADbO7lusaTg9MKpR7JKFwWEJhtpbzVPHN93gXn1XZ2HtGV5\neAoZUds8jw35PDDupz0pfP4=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-4ei9y@clinic-template-f3470.iam.gserviceaccount.com",
    "client_id": "116054239260106620919",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-4ei9y%40clinic-template-f3470.iam.gserviceaccount.com",
}

cred = credentials.Certificate(file)
initialize_app(cred)


def sendPush(title, msg, registration_token, dataObject):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(title=title, body=msg),
        data=dataObject,
        tokens=registration_token,
    )
    messaging.send_multicast(message)


# ---------------------------------------------------------------- example fcm sender
# dataObject 3aml zay id ll notification 3shan lw fe aktr mn no3 notification fel app fa nb2a 3rfen kol notification el mfrod ywdena anhy sf7a
# dataObject = {"click_action": "FLUTTER_NOTIFICATION_CLICK"}
# ___________________________EXAMPLE________________________
# dataObject = None
# tokens = []
# sendPush(
#     "title",
#     "descreption",
#     tokens,
#     dataObject,
# )
# ___________________________END EXAMPLE________________________
