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
        # api_key='llx-h1i19WInubxNtdmxQRoNYunacafCmusPpxrpvMQk84yCGrx0',
        # api_key = 'llx-U0Z4fThyevjvtauoo5YLJ9NkhnOsOwic770Mpfg7OoQwM1Yf',
        # api_key = 'llx-gIl0PkklvC87KCJusA2BpHetHHAM2vxILL5W3G6UgHld1tCY',
        api_key="llx-BrwPD5pXet4ht1PErRu3iisqIC1az60y46rjKsq7VmMHsEfP",  # Huzaifa
        result_type=ResultType.MD,  # Options: "markdown" or "text"
        verbose=True,
        num_workers=4,
        split_by_page=False,
        # user_prompt="use single hash for main headings only and donot use double hash or triple hash for subheadings leave them as they are",
        # use_vendor_multimodal_model=True,
        # vendor_multimodal_model_name="",
        # gpt4o_mode=True,
        user_prompt="""
Parse the document into Markdown using the exact structure and heading levels shown below.

### Parsing Rules:
1. Preserve heading hierarchy exactly:
   - `#` for the main fund title (e.g., "# Alfalah GHP Cash Fund")
   - `##` for main sections (e.g., "## Basic Information")
   - `###` for subsections (if any)
2. Do not merge or downgrade headings (for example, don't change `##` to `#`).
3. Maintain all Markdown formatting:
   - Keep all tables in Markdown format using `|` and `---`.
   - Keep line breaks and spacing as shown.
4. Extract data **only** from the provided input document.
5. **Do not copy, reuse, or fill in any example data from the template below.**
6. Do not summarize, rephrase, or infer missing details.
7. Output only the parsed Markdown text — no commentary or extra text.

### Output Template  
**(Use this structure as a reference only. Do NOT copy or include any data from this example — only follow its formatting and layout.)**

---
# Fund Managers’ Report

## March, 2025

### Alfalah Investments

## _Note: Additional details about the fund and its performance will be provided in the subsequent sections._

# Alfalah Asset Management Limited

## Risk Profile of Conventional Collective Investment Schemes/Plans

| Fund Name                                 | Scheme Type                           | Risk Profile | Principal Risk Level     |
| ----------------------------------------- | ------------------------------------- | ------------ | ------------------------ |
| Alfalah GHP Alpha Fund                    | Equity Scheme                         | High         | Principal at high risk   |
| Alfalah GHP Value Fund                    | Asset Allocation Scheme               | High         | Principal at high risk   |
| Alfalah Financial Value Fund              | Asset Allocation Scheme               | High         | Principal at high risk   |
| Alfalah Asset Allocation Fund             | Asset Allocation Scheme               | High         | Principal at high risk   |
| Alfalah GHP Stock Fund                    | Equity Scheme                         | High         | Principal at high risk   |
| Alfalah GHP Stock Fund-II                 | Equity Scheme                         | High         | Principal at high risk   |
| Alfalah GHP Sovereign Income Fund         | Income Scheme                         | Medium       | Principal at medium risk |
| Alfalah MTS Fund                          | Income Scheme                         | Low          | Principal at medium risk |
| Alfalah Saving Growth Fund                | Income Scheme                         | Medium       | Principal at medium risk |
| Alfalah Government Securities Fund - I    | Sovereign Income Scheme               | Low          | Principal at low risk    |
| Alfalah Government Securities Fund - II   | Sovereign Income Scheme               | Low          | Principal at low risk    |
| Alfalah GHP Consumer Index ETF            | Exchange Traded Fund                  | High         | Principal at high risk   |
| Alfalah GHP Money Market Fund             | Money Market Scheme                   | Low          | Principal at low risk    |
| Alfalah GHP Money Market Fund - II        | Money Market Scheme                   | Low          | Principal at low risk    |
| Alfalah GHP Income Multiplier Fund        | Aggressive Income Scheme              | Medium       | Principal at medium risk |
| Alfalah Income & Growth Fund              | Aggressive Income Scheme              | Medium       | Principal at medium risk |
| Alfalah Financial Sector Income Plan - 2  | Income Scheme                         | Medium       | Principal at medium risk |
| Alfalah Stable Return Fund Plan 10        | Fixed Return Scheme                   | Low          | Principal at low risk    |
| Alfalah Stable Return Fund Plan 12        | Fixed Return Scheme                   | Low          | Principal at low risk    |
| Alfalah Stable Return Fund Plan 13        | Fixed Return Scheme                   | Low          | Principal at low risk    |
| Alfalah Stable Return Fund Plan 14        | Fixed Return Scheme                   | Low          | Principal at low risk    |
| Alfalah Stable Return Fund Plan 15        | Fixed Return Scheme                   | Low          | Principal at low risk    |
| Alfalah Stable Return Fund Plan 17        | Fixed Return Scheme                   | Low          | Principal at low risk    |
| Alfalah Stable Return Fund Plan 18        | Fixed Return Scheme                   | Low          | Principal at low risk    |
| Alfalah Stable Return Fund Plan 19        | Fixed Return Scheme                   | Low          | Principal at low risk    |
| Alfalah GHP Income Fund                   | Income Scheme                         | Medium       | Principal at medium risk |
| Alfalah Financial Sector Opportunity Fund | Income Scheme                         | Medium       | Principal at medium risk |
| Alfalah GHP Cash Fund                     | Money Market Scheme                   | Low          | Principal at low risk    |
| Alfalah GHP Cash Fund - II                | Money Market Scheme                   | Low          | Principal at low risk    |
| Alfalah GHP Dedicated Equity Fund         | Equity Scheme                         | High         | Principal at high risk   |
| Alfalah Strategic Allocation Plan – I     | Asset Allocation Fund of Funds Scheme | High         | Principal at high risk   |
| Alfalah GHP Prosperity Planning Fund      | Fund of Funds Scheme                  | High         | Principal at high risk   |
| a) Active Allocation Plan                 | Fund of Funds Scheme                  | High         | Principal at high risk   |
| b) Moderate Allocation Plan               | Fund of Funds Scheme                  | Medium       | Principal at medium risk |
| c) Conservative Allocation Plan           | Fund of Funds Scheme                  | Medium       | Principal at medium risk |
| d) Capital Preservation Plan - 4          | Fund of Funds Scheme                  | Medium       | Principal at medium risk |
| Alfalah GHP Pension Fund                  | Voluntary Pension Fund Scheme         |              |                          |
| a) Equity Sub Fund                        |                                       | High         | Principal at high risk   |
| b) Debt Sub Fund                          |                                       | Medium       | Principal at medium risk |
| c) Money Market Sub Fund                  |                                       | Low          | Principal at low risk    |
| Alfalah GHP Pension Fund - II             | Voluntary Pension Fund Scheme         |              |                          |
| a) Equity Sub Fund                        |                                       | High         | Principal at high risk   |
| b) Debt Sub Fund                          |                                       | Medium       | Principal at medium risk |
| c) Money Market Sub Fund                  |                                       | Low          | Principal at low risk    |
| Alfalah Financial Sector Income Plan - 1  | Income Scheme                         | Medium       | Principal at medium risk |
| Alfalah Government Securities Fund        | Income Scheme                         | Medium       | Principal at medium risk |
| Alfalah KPK Employee Pension Fund         | Voluntary Pension Fund Scheme         |              |                          |
| Money Market Sub Fund                     |                                       | Low          | Principal at low risk    |

# Alfalah Asset Management Limited Fund Managers' Report

Economic & Capital Markets Review

### Economic Review & Outlook

March 2025 brought encouraging developments for Pakistan’s economy, particularly on the external front. Exports rose by 5.1% month-on-month to USD 2.62 billion, while imports dipped slightly by 1.1% to USD 4.74 billion. As a result, the trade deficit narrowed by 7.8% to USD 2.1 billion. With strong remittance inflows during Ramazan, the current account has recorded a surplus of USD 691 million in the first eight months of FY25. Despite this progress, foreign exchange reserves fell by USD 550 million to USD 10.7 billion, mainly due to debt repayments.

On the inflation front, consumer prices showed a notable cooling. Headline CPI inflation eased to 0.69% in March—down from 1.52% in February—registering the lowest reading since December 1965. Core inflation remained unchanged at 8.98%. Though the recent drop is mostly due to base effects, a slight uptick in inflation is anticipated toward the end of the fiscal year. We expect CPI for FY25 to average around 5%-6%, a considerable decline from the 23.4% recorded in FY24.

In parallel, Pakistan made strides in its engagement with the IMF. A staff-level agreement was reached covering the first review of the ongoing 37-month Extended Fund Facility (EFF), along with a new 28-month Resilience and Sustainability Facility (RSF) program. This combined arrangement is expected to unlock approximately USD 1.3 billion, pending approval by the IMF Executive Board. An IMF mission is also anticipated in the coming months to assist with the formulation of the federal budget for FY2025-26.

### Money Market Review & Outlook

Since June 2024, the SBP has reduced the policy rate by a total of 1,000 basis points, lowering the policy rate from 22.0% to 12.0%. The recent drop in global oil prices may provide additional downward pressure on inflation. However, while the outlook for inflation and imports has improved, potential weaknesses in exports and remittances, coupled with global economic uncertainties, may offset these gains. We expect the SBP to closely monitor these dynamics and make policy adjustments aimed at achieving a balance between macroeconomic stability and growth.

Short-term secondary market yields and longer-tenor yields rose during the month. The 3M PKRV increased by 68 basis points, 6M PKRV by 103 basis points, 1Y PKRV increased by 129 basis points, and 3Y PKRV increased by 136 basis points. This uptick in yields came after the State Bank of Pakistan (SBP) decided to keep the monetary policy unchanged in its meeting on March 10, 2025, despite mixed market expectations. The SBP maintained the current interest rate, citing persistent core inflation between 8%-9%, and expressed concerns in case of rising food and energy prices could contribute to further inflationary pressures.

SBP conducted a Treasury bill auction on March 26, 2025, with a total maturity of PKR 412 billion against a target of PKR 650 billion. The central bank accepted bids totaling PKR 226 billion for 1-month bills, PKR 111 billion for 3-month bills, PKR 74 billion for 6-month bills, and PKR 195 billion for 12-month bills. The cut-off yields for these bills were 12.39%, 12.01%, 12.00%, and 12.01%, respectively. These rates were up by an average of 29 basis points compared to the previous auction.

Additionally, SBP held an auction for fixed coupon PIB bonds on March 12, 2025, with a total maturity of PKR 70 billion against a target of PKR 350 billion. The bank accepted bids worth PKR 6 billion for 5-year bonds and PKR 10 billion for 10-year bonds, with cut-off rates of 12.37% and 12.79%, respectively.

We anticipate a cumulative reduction of 1% to 2% in the policy rate by December 2025, primarily driven by the Central Bank’s long-term inflation expectations in the range of 5%-7%. However, core inflation has remained persistently high, hovering around 9%, which may limit the pace and extent of monetary easing. Additionally, recent escalations in global trade tensions could prompt the Central Bank to adopt a more cautious stance.

### Equity Market Review & Outlook

March 2025 brought a strong performance for the Pakistan Stock Exchange, with the KSE-100 Index achieving a record high of 118,769 points before closing the month at 117,807 points. This translated into a healthy 4.0% gain on a monthly basis, reflecting growing market confidence fueled by several key economic developments.

Momentum picked up early in the month following news of a government agreement with commercial banks to resolve a significant portion—PKR 1.2 trillion—of circular debt through subsidized debt arrangements. The rally gained further traction with the announcement of a staff-level agreement between Pakistan and the IMF under the Extended Fund Facility (EFF), alongside the approval of a USD 1.3 billion Resilience and Sustainability Facility (RSF).

Sector-wise, gains were primarily driven by Exploration & Production (E&P), Oil Marketing Companies (OMCs), and Banks, which together contributed more than 3,400 points to the index’s rise. On the flip side, Fertilizers, Leather, and Investment Companies dragged performance slightly, resulting in a modest cumulative pullback.

Despite this positive backdrop, market participation was somewhat restrained due to the shortened trading schedule during Ramazan. Daily average volumes dropped to 366 million shares, a 28.9% decline from the previous month, meanwhile, the average daily traded value held firm at USD 87 million. On the institutional side, foreign investors maintained their selling stance, leading to net outflows of USD 12 million. Among local players, Mutual Funds and Insurance firms reduced their exposure, while Banks and DFIs emerged as net buyers, balancing the overall sentiment.

The valuation backdrop remains highly attractive. The KSE-100 is currently trading at a forward P/E ratio of 6.5x, backed by improving fundamentals and a gradually stabilizing macroeconomic environment.

### Disclaimer

This publication is for informational purposes only and nothing herein should be construed as a solicitation, recommendation, or an offer to buy or sell any fund. All investments in mutual funds are subject to market risks. The NAV based prices of units and any dividends/returns thereon are dependent on forces and factors affecting the capital markets. These may go up or down based on market conditions. Past performance is not necessarily indicative of future results. Use of the name and logo of Bank Alfalah Limited as given above does not mean that it is responsible for the liabilities/obligations of Alfalah Asset Management Limited.

# Alfalah GHP Cash Fund

Fund Stability Rating: "AA+(f)" by PACRA 27-September-24

AMC Rating: "AM1" by VIS 02-Jan-25

AMC Rating: "AM1" by PACRA 30-August-24

## Investment Objective

The investment objective of Alfalah GHP Cash Fund (AGCF) is to provide a regular stream of income at a comparative rate of return while preserving capital to the extent possible by investing in assets with low risk and a high degree of liquidity from a portfolio constituted of mostly money market securities and placements.

## Basic Information

| Category:                | Money Market Scheme                                                                                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fund Type:               | Open Ended                                                                                                                                                        |
| New Benchmark:           | 90% three (3) months PKRV rates + 10% three (3) months average of the highest rates on savings account of three (3) AA rated scheduled Banks as selected by MUFAP |
| Old Benchmark:           | 70% 3month PKRV rates + 30% 3-months average deposit rates of 3 'AA' rated schedule banks as selected by MUFAP                                                    |
| Min. Initial Investment: | PKR 500/-                                                                                                                                                         |
| Min. Subseq. Investment: | PKR 100/-                                                                                                                                                         |
| Trustee:                 | CDC Pakistan Limited                                                                                                                                              |
| Auditor:                 | Yousuf Adil Chartered Accountants                                                                                                                                 |
| Front end Load:          | 2.00%                                                                                                                                                             |
| Back end Load:           | 0.00%                                                                                                                                                             |
| Same Day:                | 10:00 am                                                                                                                                                          |
| Risk Profile:            | Low                                                                                                                                                               |
| Management Fee:          | up to 1.50% per annum of the average daily net assets                                                                                                             |
| Launch Date:             | March 12, 2010                                                                                                                                                    |
| Par Value:               | PKR 500                                                                                                                                                           |
| Pricing:                 | Backward                                                                                                                                                          |
| Dealing Days:            | Monday - Friday                                                                                                                                                   |
| Cut-off Time:            | 9:00 am - 4:00 pm                                                                                                                                                 |
| Leverage:                | Nil                                                                                                                                                               |

## Investment Committee

| Name                         | Designation                     |
| ---------------------------- | ------------------------------- |
| Khaldoon Bin Latif           | Chief Executive Officer         |
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

| Fund Size (PkR mn; as on March 31, 2025)          | 4,528.1 |
| ------------------------------------------------- | ------- |
| Fund size including fund of fund schemes (PkR mn) | 4,528.2 |
| NAV (PkR)                                         | 561.5   |
| Wtd. Average Maturity (Days)                      | 45.78   |
| Total Expense Ratio (YTD)                         | 1.86%   |
| Total Expense Ratio (Month)                       | 1.70%   |

## Fund Performance

| Fund Performance           | BM     | AGCF   |
| -------------------------- | ------ | ------ |
| Since Inception Return\*   | 9.23%  | 10.48% |
| YTD                        | 15.59% | 15.15% |
| Month - New (March, 2025): | 11.69% | 9.43%  |
| Month - Old (March, 2025): | 10.03% | -      |

Avg. Peer Group Return for March 2025 was 9.91%

## Credit Quality (as % of Total Assets)

| Credit Rating                | Percentage | Credit Rating | Percentage |
| ---------------------------- | ---------- | ------------- | ---------- |
| Govt. Securities (Rated AAA) | 93.35%     | A1+           | 0.00%      |
| AAA                          | 6.32%      | A1            | 0.00%      |
| AA+                          | 0.00%      | A-            | 0.00%      |
| AA                           | 0.01%      | BBB+          | 0.00%      |
| AA-                          | 0.00%      | BBB           | 0.00%      |
| A+                           | 0.00%      | IG            | 0.00%      |
| A                            | 0.00%      | NR/UR         | 0.32%      |

## Monthly Returns

| Month  | AGCF   | BM     |
| ------ | ------ | ------ |
| Mar-24 | 18.58% | 20.59% |
| Apr-24 | 19.63% | 20.77% |
| May-24 | 20.14% | 20.54% |
| Jun-24 | 19.73% | 19.73% |
| Jul-24 | 19.43% | 19.48% |
| Aug-24 | 18.60% | 18.47% |
| Sep-24 | 20.77% | 17.20% |
| Oct-24 | 16.00% | 15.56% |
| Nov-24 | 14.42% | 14.17% |
| Dec-24 | 11.67% | 12.50% |
| Jan-25 | 9.89%  | 11.72% |
| Feb-25 | 9.48%  | 11.66% |
| Mar-25 | 9.43%  | 11.69% |

## Dispute Resolution/Complaint Handling

"Investors may lodge their complaints to our Investor Services Department through any of the following options where our dedicated staff is available to provide assistance: Call us at (+92-21) 111 090 090, Email us at complaint@alfalahamc.com, Contact us at 0300-0707417 or submit through our website https://www.alfalahamc.com/complain. In case your concerns are not settled or resolved, you may lodge your complaint with SECP at the link https://sdms.secp.gov.pk/. Please note that SECP will entertain only those complaints which were at first directly requested to be redressed by us and were not resolved as per investor satisfaction."

## Disclaimer

This publication is for informational purposes only and nothing herein should be construed as a solicitation, recommendation or an offer to buy or sell any fund. All investments in mutual funds are subject to market risks. The NAV based prices of units and any dividends/returns thereon are dependent on forces and factors affecting the capital markets. These may go up or down based on market conditions. Past performance is not necessarily indicative of future results.

\*Since Inception return is calculated on Compounded Annual Growth Rate (CAGR)

\*\*This includes 0.300% representing government levy and SECP Fee

\*\*\*Management fee of the fund has been amended from Oct 28, 2023 through 12th supplemental OD with consent of the SECP

**\***Actual Management fee charged: 1.19% of net assets

Selling & marketing expense - for the period ended March, 2025, PKR Mn 0.153

Alfalah Asset Management Ltd. (formerly Alfalah GHP Investment Management Limited)
---
""",
    )
    print(parser.api_key)

    # Define the file extractor for PDF files using LlamaParse
    file_extractor = {".pdf": parser}

    # Create a SimpleDirectoryReader to read files from the specified directory
    reader = SimpleDirectoryReader(
        "data",
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


directory = "output"
docs = pre_processing(directory)
