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
        parsing_instruction="""
         --- Fund Parsing Template ---
         
            Fund Managers’ Report
            October 2023

            # Alfalah GHP Money Market Fund

            Fund Stability Rating: "AA+ (f)" by PACRA 17 - Jun - 25

            AMC Rating: "AM1" by VIS 02-Jan-25

            AMC Rating: "AM1" by PACRA 29-August-25

            ## Investment Objective

            An open-ended Money Market Scheme which shall seek to generate competitive returns consistent with low risk from a portfolio constituted of short term instruments including cash deposits, money market placements and government securities. The Fund will maintain a high degree of liquidity, with time to maturity of single asset not exceeding six months and with weighted average time to maturity of Net Assets not exceeding 90 days.

            ## Basic Information

            | Category:                | Money Market Scheme                                                                                                                                                |
            | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
            | Fund Type:               | Open Ended                                                                                                                                                         |
            | Benchmark:               | 90% three (3) months PKRV rates + 10% three (3) months average of the highest rates on savings account of three (3) AA rated scheduled Banks as selected by MUFAP. |
            | Sales Load:              | up to 2.00%                                                                                                                                                        |
            | Risk Profile:            | Low                                                                                                                                                                |
            | Management Fee\*\*\*:    | Upto 1.25% of average net assets of the Scheme.                                                                                                                    |
            | Min. Initial Investment: | PKR 500/-                                                                                                                                                          |
            | Min. Subseq. Investment: | PKR 100/-                                                                                                                                                          |
            | Trustee:                 | CDC Pakistan Limited                                                                                                                                               |
            | Launch Date:             | May 27, 2010                                                                                                                                                       |
            | Auditor:                 | Yousuf Adil Chartered Accountants                                                                                                                                  |
            | Par Value:               | PKR 100                                                                                                                                                            |
            | Listing:                 | Pakistan Stock Exchange                                                                                                                                            |
            | Pricing:                 | Forward Day                                                                                                                                                        |
            | Dealing Days:            | Monday - Friday                                                                                                                                                    |
            | Cut-off Time:            | 9:00 am - 4:00 pm                                                                                                                                                  |
            | Leverage:                | Nil                                                                                                                                                                |

            ## Investment Committee

            | Khaldoon Bin Latif           | Chief Executive Officer         |
            | ---------------------------- | ------------------------------- |
            | Ayub Khuhro                  | Chief Investment Officer        |
            | Faisal Ali Khan              | Chief Financial Officer         |
            | Shariq Mukhtar Hashmi        | Chief Compliance Officer        |
            | Imad Ansari                  | Chief Risk Officer              |
            | Muddasir Ahmed Shaikh        | Head of Equities                |
            | Mustafa Kamal                | Head of Fixed Income            |
            | Shams-ud-din Shah, CFA, FCCA | Head of Research                |
            | Salman Jawaid                | Fund Manager Fixed Income Funds |
            | Anil Kumar, CFA              | Fund Manager Equity Funds       |

            ## Fund Statistics

            | Fund Size (PkR mn; as on Aug 31, 2025):            | 91,012  |
            | -------------------------------------------------- | ------- |
            | Fund size including fund of fund schemes (PkR mn): | 91,227  |
            | July August NAV(PkR):                              | 100.682 |
            | Information Ratio:                                 | 0.009   |
            | Portfolio Turnover:                                | 113%    |
            | Wtd. Average Maturity (Days):                      | 35.73   |
            | YTM:                                               | 9.98%   |
            | Duration:                                          | 0.089   |
            | Modified Duration:                                 | 0.081   |

            ## Fund Performance

            |                           | BM     | AGMMF  |
            | ------------------------- | ------ | ------ |
            | Since Inception Return \* | 9.30%  | 10.62% |
            | 5-Year                    | 13.70% | 14.51% |
            | 3-Year                    | 17.06% | 17.86% |
            | YTD                       | 10.67% | 9.90%  |
            | Month (Aug'25):           | 10.65% | 9.97%  |

            ## Credit Quality (as % of Total Assets)

            | Govt. Securities (Rated AAA) | 76.34% |
            | ---------------------------- | ------ |
            | AAA                          | 11.46% |
            | A1+                          | 1.77%  |
            | A1                           | 0.42%  |
            | AA+                          | 9.44%  |
            | A-                           | 0.00%  |
            | AA-                          | 0.00%  |
            | BBB+                         | 0.00%  |
            | BBB                          | 0.00%  |
            | Below                        | 0.00%  |
            | IG                           | 0.00%  |
            | A+                           | NR/U   |
            | A                            | 0.00%  |
            | R                            | 0.56%  |

            ## Monthly Returns

            |       | Aug-24 | Sep-24 | Oct-24 | Nov-24 | Dec-24 | Jan-25 | Feb-25 | Mar-25 | Apr-25 | May-25 | Jun-25 | Jul-25 | Aug-25 |
            | ----- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
            | AGMMF | 18.24% | 20.52% | 16.69% | 15.06% | 12.64% | 10.77% | 10.16% | 10.25% | 10.93% | 11.50% | 9.93%  | 9.76%  | 9.97%  |
            | BM    | 18.47% | 17.20% | 15.56% | 14.17% | 12.50% | 11.72% | 11.66% | 11.69% | 11.78% | 11.19% | 10.84% | 10.68% | 10.65% |

            ## Dispute Resolution/Complaint Handling

            “Investors may lodge their complaints to our Investor Services Department through any of the following options where our dedicated staff is available to provide assistance: Call us at (+92-21) 111 090 090, Email us at complaint@alfalahamc.com, Contact us at 0300-0707417 or submit through our website https://www.alfalahamc.com/complain. In case your concerns are not settled or resolved, you may lodge your complaint with SECP at the link https://sdms.secp.gov.pk/. Please note that SECP will entertain only those complaints which were at first directly requested to be redressed by us and were not resolved as per investor satisfaction.”

            ## Disclaimer

            This publication is for informational purposes only and nothing herein should be construed as a solicitation, recommendation or an offer to buy or sell any fund. All investments in mutual funds are subject to market risks. Past performance is not necessarily indicative of future results. Please read the Offering Document to understand the investment policies and risks involved. All returns are calculated assuming reinvested dividends. Performance data does not include the cost incurred directly by an investor in the form of sales load etc. Please be advised that the sales load (including Front End Load, Back End Load and Contingent Load) up to 3.00% or 1.50% as may be applicable, may be charged on the investment and/or upon redemption of funds, at the discretion of the management company.

            ## Total Expense Ratio Breakup

            |     |       | Regulatory Fee | Trustee Fee | Levies and Taxes | Transaction Expenses | Third Party Expenses | Other Expenses | Total TER with levies | Total TER without levies |
            | --- | ----- | -------------- | ----------- | ---------------- | -------------------- | -------------------- | -------------- | --------------------- | ------------------------ |
            | MTD | 0.78% | 0.07%          | 0.06%       | 0.13%            | 0.01%                | 0.00%                |                | 1.04%                 | 0.92%                    |
            | YTD | 0.76% | 0.07%          | 0.06%       | 0.12%            | 0.01%                | 0.00%                |                | 1.03%                 | 0.91%                    |

            - Since Inception return is calculated on Compounded Annual Growth Rate (CAGR)

            \*\*\* Management fee of the fund has been amended from Jul 01, 2025 through 18th supplemental OD with consent of the SECP

            Alfalah Investments

            Alfalah Asset Management Ltd. (formerly Alfalah GHP Investment Management Limited) Fund Managers' Report August 31, 2025
            

--- Fund Parsing Template ---



""",
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
