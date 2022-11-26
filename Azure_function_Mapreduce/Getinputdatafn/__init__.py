import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def main(name: str) -> list[tuple[int, str]]:
    try:
        print("Azure Blob Storage Python quickstart sample")
        connect_str = 'DefaultEndpointsProtocol=https;AccountName=jkmapreduce;AccountKey=MANvXfbkT4P8SbWsB2Ae5eju8g9nTTFRgh5HJTQRSN8RObaUsS9uJ7nLW+UCs/tkUzqI8f1Q3a6S+ASt1sv8mQ==;EndpointSuffix=core.windows.net'
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_container_client(container="jkblob")
        blob_list = blob_client.list_blobs()

    except Exception as ex:
        print('Exception:')
        print(ex)
    
    empty_list = []
    for blob in blob_list:
        file = blob_client.download_blob(blob.name).content_as_text()
        val = file.splitlines()
        offset = list(range(1, len(val)))
        empty_list = empty_list + list(zip(offset, val))

    return empty_list  
