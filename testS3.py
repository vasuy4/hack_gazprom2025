import boto3

key = ""
secret = ""

# Создаём клиент S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=f'tenant_id:{key}',
    aws_secret_access_key=secret,
    endpoint_url='https://s3.cloud.ru',
    region_name='ru-central-1',
)

bucket_name = 'bucket-e17927'
object_key = 'salome.png'
# Получаем объект из бакета
response = s3_client.get_object(Bucket=bucket_name, Key=object_key)

# Читаем содержимое объекта (например, если это текст)
content = response['Body'].read().decode('utf-8')

print(content)
