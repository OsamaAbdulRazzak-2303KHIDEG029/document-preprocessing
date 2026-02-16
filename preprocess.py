from llama_index.core import (
    SimpleDirectoryReader,
)
import os
from llama_parse import LlamaParse, ResultType
from llama_index.core.prompts import PromptTemplate

# from llama_index.vector_stores.chroma import ChromaVectorStore
from dotenv import load_dotenv

load_dotenv()


def pre_processing(directory):
    folder_path = f"{directory}"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    # Initialize LlamaParse with your API key
    parser = LlamaParse(
        api_key="llx-h1i19WInubxNtdmxQRoNYunacafCmusPpxrpvMQk84yCGrx0",
        # api_key = 'llx-U0Z4fThyevjvtauoo5YLJ9NkhnOsOwic770Mpfg7OoQwM1Yf',
        # api_key = 'llx-gIl0PkklvC87KCJusA2BpHetHHAM2vxILL5W3G6UgHld1tCY',
        # api_key="llx-BrwPD5pXet4ht1PErRu3iisqIC1az60y46rjKsq7VmMHsEfP",  # Huzaifa
        result_type=ResultType.MD,  # Options: "markdown" or "text"
        verbose=True,
        num_workers=4,
        split_by_page=False,
        user_prompt="""
        Formatting Rules:
            1. Use the same heading hierarchy as the template:
            - `#` → Fund title (e.g., `# Alfalah GHP Money Market Fund`)
            - `##` → Major sections (e.g., `## Basic Information`, `## Fund Performance`)
            2. Tables must use the pipe (`|`) format with proper alignment.
            3. Preserve percentage signs (%), special characters (&, *, etc.), quotes, and brackets.
            4. Maintain original line breaks for readability.
            5. Donot copy and paste the example template from system_prompt into the file  **Strickly note**
                
                """,
        system_prompt="""
        You are an expert document parser. Extract the text from the document accurately, preserving all formatting such as headings, bullet points, tables, and special characters. Ensure that the extracted content is clear and well-structured in Markdown format. 
        Parsed the document as below mentioned template""",
        # use_vendor_multimodal_model=True,
        # vendor_multimodal_model_name="",
        # gpt4o_mode=True,
    )
    print(parser.api_key)

    # Define the file extractor for PDF files using LlamaParse
    file_extractor = {".pdf": parser}

    # Create a SimpleDirectoryReader to read files from the specified directory
    reader = SimpleDirectoryReader(
        "monthwise_file_data",
        file_extractor=file_extractor,
    )

    # Load data from the specified directory
    documents = reader.load_data()

    for index, doc in enumerate(documents):
        file_name = doc.metadata["file_name"]
        file_path = os.path.join(f"{directory}", file_name)
        print(f"file_path----------------------{file_path}")
        markdown_file_path = os.path.splitext(file_path)[0] + ".md"

        # Write the document's text content to the Markdown file
        with open(markdown_file_path, "w") as f:
            f.write(str(doc.text))
            print(f"Created Markdown file: {markdown_file_path}")

    return documents


directory = "final_processed"
docs = pre_processing(directory)
