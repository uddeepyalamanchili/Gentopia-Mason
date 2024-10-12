# importing required classes
from typing import AnyStr
import requests
from gentopia.tools.basetool import *
import os
import json


class ForexArgs(BaseModel):
    currency: str = Field(..., description="Currency code to extract the exchange Euro")

class Forex(BaseTool):
    """Tool that adds the capability to extract current exchange."""

    name = "forex_tool"
    description = ("A tool to retrieve the extract the current exchange rate.")

    args_schema: Optional[Type[BaseModel]] = ForexArgs


    def _run(self, currency: AnyStr) -> str:
        try: 
            forexApiKey = '' #<YOUR_API_KEY>
            url = f"https://data.fixer.io/api/latest?access_key={forexApiKey}&base=EUR&symbols={currency}"
            
            response = requests.get(url)
            response.raise_for_status()
            # data = json.loads(response.json())
 
            # Convert dict to string
            data = json.dumps(response.json())
            return data
        except Exception as e:
                return f"Error: {e}\n\n"



    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "__main__":
    ans = Forex()._run("USD")
    print(ans)