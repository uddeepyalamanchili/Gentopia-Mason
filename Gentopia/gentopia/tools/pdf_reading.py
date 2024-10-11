# importing required classes
from pypdf import PdfReader
from typing import AnyStr
import requests
from gentopia.tools.basetool import *

class PdfTextExtracterArgs(BaseModel):
    url: str = Field(..., description="URL to read the file")

class PdfTextExtracter(BaseTool):
    """Tool that adds the capability to extract text from a given pdf URL."""

    name = "pdf_text_extract"
    description = ("A tool to retrieve the pdf from the given URL and extract text from it.")

    args_schema: Optional[Type[BaseModel]] = PdfTextExtracterArgs


    def _run(self, url: AnyStr) -> str:
        try: 
            response = requests.get(url)
            response.raise_for_status()

            with open('file.pdf', 'wb') as f:
                f.write(response.content)


            txt = open('file.pdf', 'rb')

            read_pdf = PdfReader(txt)

            extracted_text = ""
            for page in read_pdf.pages:
                extracted_text += page.extract_text()
            print('tets')
            print(extracted_text)
            return extracted_text
        except Exception as e:
                return f"Error: {e}\n\n"



    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "__main__":
    ans = PdfTextExtracter()._run("https://arxiv.org/pdf/2201.05966")
    print(ans)