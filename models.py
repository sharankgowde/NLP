#create a model for speaker with a name, bio and linkedin URL
from PyPDF2 import PdfReader
from azure.storage.blob import BlobServiceClient



# Step 1: Read the PDF file
pdf_path = "Downloads\AIbrochure.pdf"

pdf_reader = PdfReader(pdf_path)

text = ""
for page in pdf_reader.pages:
    text += page.extract_text()


# Step 2: Connect to Azure Blob Storage
connection_string = "BlobEndpoint=https://testingstoragesharan.blob.core.windows.net/;QueueEndpoint=https://testingstoragesharan.queue.core.windows.net/;FileEndpoint=https://testingstoragesharan.file.core.windows.net/;TableEndpoint=https://testingstoragesharan.table.core.windows.net/;SharedAccessSignature=sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-09-22T21:04:35Z&st=2023-09-15T13:04:35Z&spr=https,http&sig=xjH3m7cqronJGE5M2Y8cIDoNge0JE2hojZlo%2BkECLUQ%3D"
container_name = "pdfcontent"
blob_name = "AIbrochure.pdf"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

# Step 3: Upload the PDF content to Blob Storage
blob_client = container_client.get_blob_client(blob_name)

# Upload the PDF content
blob_client.upload_blob(text, overwrite=True)