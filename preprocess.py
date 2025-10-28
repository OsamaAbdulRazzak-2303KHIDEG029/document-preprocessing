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
        user_prompt="""
        You are an expert document parser. Extract the text from the document accurately, preserving all formatting such as headings, bullet points, tables, and special characters. Ensure that the extracted content is clear and well-structured in Markdown format.
        here is example
        October 2023

Alfalah Asset Management Limited

## (formerly Alfalah GHP Investment Management Limited)

### RISK PROFILE OF CONVENTIONAL COLLECTIVE INVESTMENT SCHEMES/PLANS

| #   | Fund Name                            | Scheme Type                   | Risk Level | Principal Risk           |
| --- | ------------------------------------ | ----------------------------- | ---------- | ------------------------ |
| 1   | Alfalah GHP Alpha Fund               | Equity Scheme                 | High       | Principal at high risk   |
| 2   | Alfalah GHP Value Fund               | Asset Allocation Scheme       | High       | Principal at high risk   |
| 3   | Alfalah GHP Financial Value Fund     | Asset allocation scheme       | High       | Principal at high risk   |
| 4   | Alfalah GHP Stock Fund               | Equity Scheme                 | High       | Principal at high risk   |
| 5   | Alfalah GHP Sovereign Income Fund    | Income Scheme                 | Medium     | Principal at medium risk |
| 6   | Alfalah GHP Consumer Index ETF       | Exchange Traded Fund          | High       | Principal at high risk   |
| 7   | Alfalah GHP Money Market Fund        | Money Market Scheme           | Low        | Principal at low risk    |
| 8   | Alfalah GHP Income Multiplier Fund   | Aggressive Income Scheme      | Medium     | Principal at medium risk |
| 9   | Alfalah Stable Return Fund Plan 2    | Fixed Return Scheme           | Low        | Principal at low risk    |
| 10  | Alfalah Stable Return Fund Plan 6    | Fixed Return Scheme           | Low        | Principal at low risk    |
| 11  | Alfalah GHP Income Fund              | Income Scheme                 | Medium     | Principal at medium risk |
| 12  | Alfalah GHP Cash Fund                | Money Market Scheme           | Low        | Principal at low risk    |
| 13  | Alfalah GHP Dedicated Equity Fund    | Equity Scheme                 | High       | Principal at high risk   |
| 14  | Alfalah GHP Prosperity Planning Fund | Fund of Fund Scheme           |            |                          |
|     | a) Active Allocation Plan            | Fund of Fund Scheme           | High       | Principal at high risk   |
|     | b) Moderate Allocation Plan          | Fund of Fund Scheme           | Medium     | Principal at medium risk |
|     | c) Conservative Allocation Plan      | Fund of Fund Scheme           | Medium     | Principal at medium risk |
| 15  | Alfalah GHP Pension Fund             | Voluntary Pension Fund Scheme |            |                          |
|     | a) Equity Sub Fund                   |                               | High       | Principle at high risk   |
|     | b) Debt Sub Fund                     |                               | Medium     | Principle at medium risk |
|     | c) Money Market Sub Fund             |                               | Low        | Principle at low risk    |
| 16  | Alfalah Financial Sector Income Fund | Income scheme                 | Medium     | Principle at medium risk |

Alfalah Asset Management Limited (formerly Alfalah GHP Investment Management Limited)

Fund Managers' Report October 2023

## Economic & Capital Markets Review

### Economic Review & Outlook

Globally, the economic situation is still challenging following the Russia-Ukraine conflict, wherein the commodity prices are hovering around historic high levels. On the local front, the higher commodity prices would bring inflationary burdens and keep external account under pressure. Following the removal of subsidies on petroleum products and increase in prices by more than PKR 100, inflation for the month of Jun’22 clocked at 21.32% (highest in 14 years). Inflation is also driven by higher food prices and an uptick in housing index. Due to higher NCPI levels, secondary market yields across 3-12 months’ tenor climbed by an average of 64bps.

Foreign exchange reserves increased slightly to US$12.58bn at end of October, compared to US$12.47bn at the end of last month. PKR continued to appreciate and recovered by 2.23% during the month to close at the level of 281.47, as the stern administrative actions taken by the caretaker setup continued to bear fruits. On external front, the Current Account Deficit for the month of May-2022 clocked at US$1.4bn relative to a deficit of US$640mn in same period last year, solely attributable to higher imports. Cumulatively, current account deficit registered at US$15.2bn in 11MFY22 compared to a deficit of US$1.2bn last year. In 11MFY22, petroleum group imports witnessed growth of 99%YoY to USD19.8bn (27%YoY in volumetric terms).

Inflation for the month of October clocked at 26.9%. Housing and Food segments remained major contributors and accounted for 75% of overall monthly change. Perishable food prices including tomatoes and eggs continued to increase in response to rising inflation. While increased electricity charges contributed most to the rise in Housing segment.

Furthermore, the persistent rise in imports and in absence of foreign flows, foreign exchange reserves dropped to USD14.2bn in mid Jun’22 (lowest level since Jul-19). Due to draining foreign exchange reserves and uncertainty on foreign inflows, PKR/USD parity touched an all-time peak level of PKR211.9/USD; later it recovered to PKR204.8/USD by end of the month on back of proceeds received from China Development Bank. Resultantly, foreign exchange reserves increased to USD16.2bn.

Going forward, inflation is expected to remain at elevated levels of late 20s till January 2024, before falling below 20% in last quarter of the current fiscal year, however, the recent gas tariff hike is expected to keep the sequential trend in the positive territory. This may add pressures to WPI in the form of potential cost pass on by the affected industries. Nonetheless, despite increasing sequential inflation, the higher base set in preceding months will likely lead to disinflation during 2HFY24.

The incumbent government has recently raised domestic petroleum prices in order to reduce burden on fiscal account and to revive the stalled IMF program. Inflation is expected to remain elevated for next 6-7 months fueled by removal of subsidy on petroleum products and increase in utility tariffs. However, the recent slump in international oil prices would help in curtailing the import bill and ease pressure on external account.

### Money Market Review & Outlook

Inflation for the month of October clocked at 26.9%. Housing and Food segments remained the major contributors to the monthly change and accounted for 75% of overall MoM increase. Perishable food prices including tomatoes and eggs continued to increase in response to rising inflation. Increased electricity prices mainly contributed to increase in the electricity segment.

Going forward, inflation is expected to remain at elevated levels of late 20s till January 2024, before falling below 20% in last quarter of the current fiscal year. However, the impact of volatility in oil prices due to current Middle East conflict and increase in gas prices may result in higher than expected inflation going forward as manufacturers start to pass on the impact of cost pressures.

SBP held two T-Bill auctions during the month of October, with a target of PKR 1,500 billion against the maturity of PKR 1,437 billion. In the first auction, amount of PKR 520 billion was accepted at cut-off yields of 22.50%, 22.85% and 22.84% for 3-month, 6-month and 12 months’ tenure respectively. In the second auction, an amount of around PKR 914 billion was accepted at cut-off yields of 22.20%, 22.40% and 22.40% for 3-month, 6-month and 12-month tenures respectively.

In the PIB auction, bids worth around Rs.115 billion were realized for 3-years, 5-years and 10-years at a cut-off yield of 19.19%, 16.95% and 15.25%. However, no bids were received for 15-years, 20-years and 30-years tenures.

The Central Bank conducted a monetary policy meeting on October 30, 2023, in which the Monetary Policy Committee (MPC) decided to maintain the policy rate at 22%, citing downward trajectory of inflation going forward due to an improvement in macroeconomic indicators and effective administrative measures including the alignment of interbank and open market exchange rate. However, MPC also noted the possible key risks which can impact the inflation reading going forward including volatile trend in global oil prices, as well as the second-round effect of substantial increase in gas tariffs.

Keeping real interest rates in positive territory on forward looking basis remains key objective of the Monetary Policy Committee, as it will continue to remain vigilant and assess its stance to achieve price stability.

### Equity Market Review & Outlook

Benchmark index i.e. KSE-100 posted a handsome return of 12.3% during the month of October to close at a level of 51,920 points. The market successfully breached the psychological barrier of 50,000 after a period of more than 6 years. The average daily volume increased by 149% on MoM basis as it clocked at 189.8mn compared to previous month’s level of 76.1mn. Foreigners remained net sellers, as the net foreign outflow during the current month amounted to US$12mn compared to a net outflow of US$9mn in September, where the majority of selling was seen in Commercial banks and Technology. During the month, Commercial Banks, Fertilizers and Power generation were the top performers, contributing 1,778, 918 and 700 points, respectively.

Market responded positively to continuous appreciation of PKR which continued till first half of the month as a result of strict measures taken by the government against hoarding and smuggling. Moreover, outstanding results along with hefty payouts from index heavy weight sectors including Banks and Fertilizers increased investors’ confidence in the market, clearly depicted by 149% increase in volume of benchmark index on monthly basis.

Hike in gas prices before the IMF review also provided much needed confidence to the investors on successful completion of the upcoming quarterly review. Furthermore, the Central Bank once again decided to maintain the policy rate at 22%, citing downward trajectory of inflation going forward and signaling peaking of the interest rates.

Going forward, inflation is expected to remain at elevated levels of late 20s till January 2024, before falling below 20% in last quarter of the current fiscal year. However, the impact of increase in utility tariffs may result in higher than expected inflation as manufacturers start to pass on the impact of cost pressures.

We believe, realization of massive investments from friendly countries and expectations of commencement of monetary easing from second half of fiscal year 2024 can potentially spark a decent rally in the market. Moreover, valuation continues to remain enticing as the benchmark index i.e. KSE-100 is currently trading at a PER of 4.2x compared to long term average of 8x.

### KSE-100 Index (Monthly)

| KSE-100 (Volume ['Mn]) | KSE-100 (Closing Index) |
| ---------------------- | ----------------------- |
| 54,000                 | 26.00                   |
| 52,000                 | 24.00                   |
| 50,000                 | 22.00                   |
| 48,000                 | 20.00                   |
| 46,000                 | 18.00                   |
| 44,000                 | 16.00                   |
| 42,000                 | 14.00                   |
| 0                      | 12.00                   |

### Yield Curve (Monthly)

| Tenure     | Yield |
| ---------- | ----- |
| 0-7 days   |       |
| 15 days    |       |
| 16-30 days |       |
| 60 days    |       |
| 90 days    |       |
| 120 days   |       |
| 180 days   |       |
| 270 days   |       |
| 365 days   |       |
| 3 years    |       |
| 5 years    |       |
| 10 years   |       |
| 15 years   |       |
| 20 years   |       |
| 30 years   |       |

## Disclaimer:

This publication is for informational purposes only and nothing herein should be construed as a solicitation, recommendation or an offer to buy or sell any fund. All investments in mutual funds are subject to market risks. The NAV based prices of units and any dividends/returns thereon are dependent on forces and factors affecting the capital markets. These may go up or down based on market conditions. Past performance is not necessarily indicative of future results. Use of the name and logo of Bank Alfalah Limited as given above does not mean that it is responsible for the liabilities/ obligations of Alfalah Asset Management Limited or any investment scheme managed by it.

Alfalah Asset Management Ltd. (formerly Alfalah GHP Investment Management Limited)

October 31, 2023

# Alfalah GHP Cash Fund

Fund Stability Rating: "AA+(f)" by PACRA 28-Sept-23

AMC Rating: "AM2++" by PACRA 31-Aug-23

## Investment Objective

The investment objective of Alfalah GHP Cash Fund (AGCF) is to provide regular stream of income at comparative rate of return while preserving capital to extent possible by investing in assets with low risk and high degree of liquidity from a portfolio constituted of mostly money market securities and placements.

## Basic Information

| Category:                | Money Market Scheme                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Risk Profile:            | Low                                                                                                           |
| Fund Type:               | Open Ended                                                                                                    |
| Management Fee\*\*\*:    | up to 1.50% per annum of the average daily net assets                                                         |
| Benchmark:               | 70% 3month PKRV rates +30% 3-months average deposit rates of 3 'AA' rated schedule banks as selected by MUFAP |
| Min. Initial Investment: | PKR 500/-                                                                                                     |
| Min. Subseq. Investment: | PKR 100/-                                                                                                     |
| Launch Date:             | March 12, 2010                                                                                                |
| Trustee:                 | CDC Pakistan Limited                                                                                          |
| Par Value:               | PKR 500                                                                                                       |
| Auditor:                 | EY Ford Rhodes                                                                                                |
| Pricing\*\*\*\*:         | Backward                                                                                                      |
| Front end Load:          | 0.75%                                                                                                         |
| Back end Load:           | 0.00%                                                                                                         |
| Dealing Days:            | Monday - Friday                                                                                               |
| Cut-off Time\*\*\*\*:    | 9:00 am - 4:00 pm                                                                                             |
| Same Day:                | 10:00 am                                                                                                      |
| Leverage:                | Nil                                                                                                           |

## Fund Statistics

| Statistic                                         | Value    |
| ------------------------------------------------- | -------- |
| Fund Size (PKR mn; as on October 31, 2023)        | 4,503.1  |
| Fund size including fund of fund schemes (PKR mn) | 4,503.2  |
| NAV (PKR):                                        | 539.2868 |
| Wtd. Average Maturity (Days):                     | 26.25    |
| Total Expense Ratio (YTD)\*\*                     | 1.55%    |
| Total Expense Ratio (Month)                       | 1.67%    |

## Fund Performance

| Metric                   | BM     | AGCIF  |
| ------------------------ | ------ | ------ |
| Since Inception Return\* | 8.40%  | 9.70%  |
| YTD (October, 2023)      | 21.84% | 21.57% |
| Month                    | 21.55% | 21.06% |

## Credit Quality (as % of Total Assets)

| Rating                       | Percentage |
| ---------------------------- | ---------- |
| Govt. Securities (Rated AAA) | 87.84%     |
| AAA                          | 0.12%      |
| AA+                          | 10.45%     |
| AA                           | 0.00%      |
| AA-                          | 0.00%      |
| A+                           | 0.00%      |
| A                            | 0.00%      |
| A-                           | 0.00%      |
| BBB+                         | 0.00%      |
| BBB                          | 0.00%      |
| IG                           | 0.00%      |
| NR/UR                        | 1.59%      |

## Monthly Returns

| Month  | AGCF   | BM     |
| ------ | ------ | ------ |
| Oct-22 | 14.64% | 14.93% |
| Nov-22 | 13.36% | 14.99% |
| Dec-22 | 16.13% | 15.86% |
| Jan-23 | 15.09% | 16.29% |
| Feb-23 | 14.61% | 17.29% |
| Mar-23 | 17.80% | 19.18% |
| Apr-23 | 19.50% | 20.28% |
| May-23 | 20.06% | 20.78% |
| Jun-23 | 19.72% | 21.06% |
| Jul-23 | 21.77% | 21.75% |
| Aug-23 | 20.12% | 21.90% |
| Sep-23 | 21.08% | 22.18% |
| Oct-23 | 21.06% | 21.55% |

## Dispute Resolution/Complaint Handling

“Investors may lodge their complaints to our Investor Services Department through any of the following options where our dedicated staff is available to provide assistance: Call us at (+92-21) 111 090 090, Email us at complaint@alfalahamc.com, Contact us at 0300-0707417 or submit through our website https://www.alfalahamc.com/complain. In case your concerns are not settled or resolved, you may lodge your complaint with SECP at the link https://sdms.secp.gov.pk/. Please note that SECP will entertain only those complaints which were at first directly requested to be redressed by us and were not resolved as per investor satisfaction.”

## Disclaimer

This publication is for informational purposes only and nothing herein should be construed as a solicitation, recommendation or an offer to buy or sell any fund. All investments in mutual funds are subject to market risks. The NAV based prices of units and any dividends/returns thereon are dependant on forces and factors affecting the capital markets. These may go up or down based on market conditions. Past performance is not necessarily indicative of future results.

\*Since Inception return is calculated on Compounded Annual Growth Rate (CAGR)

\*\*This include 0.179% representing government levy and SECP Fee

\*\*\*Management fee of the fund has been amended from Oct 28, 2022 through 12th supplemental OD with consent of the SECP

**\***Actual Management fee charged: 0.75% of net assets

Selling & marketing expense - for the period ended October,2023, PKR Mn 2.427

Alfalah Asset Management Ltd. (formerly Alfalah GHP Investment Management Limited)

October 31, 2023""",
        # use_vendor_multimodal_model=True,
        # vendor_multimodal_model_name="",
        # gpt4o_mode=True,
    )
    print(parser.api_key)

    # Define the file extractor for PDF files using LlamaParse
    file_extractor = {".pdf": parser}

    # Create a SimpleDirectoryReader to read files from the specified directory
    reader = SimpleDirectoryReader(
        "data_1",
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


directory = "output_1"
docs = pre_processing(directory)
