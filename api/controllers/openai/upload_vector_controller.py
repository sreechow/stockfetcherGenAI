import requests
from io import BytesIO
from openai import OpenAI

client = OpenAI()

def create_file(client, file_path):
    if file_path.startswith("http://") or file_path.startswith("https://"):
        # Download the file content from the URL
        response = requests.get(file_path)
        file_content = BytesIO(response.content)
        file_name = file_path.split("/")[-1]
        file_tuple = (file_name, file_content)
        result = client.files.create(
            file=file_tuple,
            purpose="assistants"
        )
    else:
        # Handle local file path
        with open(file_path, "rb") as file_content:
            result = client.files.create(
                file=file_content,
                purpose="assistants"
            )
    print("file id", result.id)
    return result.id

def upload_and_create_vector_store(file_path):
    try:
        # Replace with your own file path or URL
        file_id = create_file(client, file_path)

        # Create a vector store
        vector_store = client.vector_stores.create(name="stock_projections_base") #name can be anything
        print(vector_store.id)

        # Add file to the vector store
        result = client.vector_stores.files.create(
            vector_store_id=vector_store.id,
            file_id=file_id
        )
        print(result)
        return result
    except Exception as e:
        print(e)
        return str(e)