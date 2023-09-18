<span style="font-family:Times New Roman; font-size:14pt;">
<h2 align="center"><b>Flight Data Analysis</b></h2>
</span>



<span style="font-family:Times New Roman; font-size:15pt;">
<h4><b>1. Problem and Data<b></h4>
<span>
<span style="font-family: Times New Roman; font-size: 13pt;">

In this GitHub repository, you will find the culmination of a data analysis project centered around airline ticket data. The dataset comprises various attributes, including user IDs, purchase dates and times, ticket information, airline codes, source and destination codes, and pricing details. The primary objective of this project is to extract meaningful insights from this data through Python-based analysis, leveraging libraries like Pandas for data manipulation and computation.

<span style="font-family:Times New Roman; font-size:15pt;">
<h4><b>2. Questions and Objectives<b></h4>
<span>
<span style="font-family: Times New Roman; font-size: 13pt;">

The project revolves around answering a series of questions and fulfilling specific objectives to gain a comprehensive understanding of the dataset. Below, we outline the key inquiries we aim to address:

* Monthly Buying and Selling Analysis: We seek to calculate the average monthly expenditure and revenue for each customer while examining whether these metrics are influenced by the specific day of the month when the purchase was made. This entails converting Gregorian dates to their corresponding day values.

* Customer Club Points: To determine the most esteemed customers, we set a purchase threshold, such as transactions exceeding 900,000 tomans, and assign points based on these criteria.

* Sales Analysis by Day and Time: We analyze sales patterns across different days of the week and hours of the day to pinpoint the most and least popular timeframes for transactions.

* Purchase and Ticket Date Analysis: This analysis centers around the temporal gap between purchase and ticket issuance, categorized by months. We aim to unveil insights into customer behavior and supplier service levels.

* Popular Routes: Identifying the most frequented routes is essential. We delve into this aspect and explore the relationships between these popular routes and their corresponding origins and destinations.

* Airlines Performance Analysis: We scrutinize the popularity and profitability of airlines, scrutinizing variations across different months, origins, and destinations to inform resource allocation decisions.

Each of these questions is tackled using Python programming and Pandas data manipulation, with the results and insights documented in the respective sections of this repository. By addressing these questions, we aim to provide valuable insights that can guide decision-making processes within the context of the airline industry. It is essential to remember that the responsible and ethical use of data is paramount, ensuring compliance with all privacy regulations and ethical guidelines.

</span>


<span style="font-family:Times New Roman; font-size:15pt;">
<h4><b>3. Data Transformation and Code Structure<b></h4>
<span>
<span style="font-family: Times New Roman; font-size: 13pt;">

The provided dataset underwent certain transformations to meet the project's specific requirements. These transformations were facilitated by the "timecalc" module, which was custom-designed for this purpose. This module adds several essential columns to the primary data, including month, year, day, week, time of ticket purchase, flight time, and the duration between purchase and flight. Additionally, the module undertakes the conversion of Gregorian calendar months to their corresponding solar calendar counterparts.

The project's codebase is organized into various modules, ensuring flexibility and ease of use. If anyone wishes to analyze their own dataset following the structure of this project, they can effortlessly do so by invoking these modular functions. This approach allows for seamless integration of the provided code with diverse datasets, ensuring that updates to the dataset will not disrupt the analysis process.

* timecalc module: This module leverages the datetime library and Pandas to create specialized columns in the data. Functions include:
  - `Sharhighharbi(data)`: Converts Gregorian months and days to the solar calendar, influencing subsequent functions.
  - `Rooz(data)`: Adds a column for the solar day of the week corresponding to the purchase date.
  - `Mah(data)`: Incorporates a column for solar months based on the purchase date.
  - `Sal(data)`: Adds a column indicating the solar year of the purchase.
  - `Time(data)`: Appends the exact time of ticket purchase to the data.
  - `Departure_time(data)`: Adds a column containing the exact time of the flight.
  - `Timedelta(data)`: Incorporates a column indicating the time interval between purchase and flight.

* Customers module: This module employs Pandas to define five functions. Notably:
  - `pointset(data)`: Assigns points to passengers based on purchase amounts within predefined ranges, determined by the user.
  - `Pointkolli(data)`: Provides overall points to each customer irrespective of the airline.
  - `Pointwithcompanydevide(data)`: Assigns points to customers of each airline based on average and quartiles of sales.
  - `Percentset(data)`: Sets the maximum discount a company can offer, typically at 10 percent.
  - `Offpercentwithcompanydevide(data)`: Calculates discounts for each company based on purchase statistics and time difference between ticket purchase and flight.

* Timeanalysis module: This module comprises 15 functions, offering insights into purchases and sales across various time periods. Functions include:
  - `monthpersianbyusercount(data)`: Provides the number of purchased tickets in each solar month.
  - Other functions offer metrics like the number of purchases per day of the week, month, hour, and night, as well as average purchase prices and total purchases by these time frames, along with the average difference between the flight and purchase date.

* Commute module: This module contains 8 functions primarily focused on origin, destination, and their relationship. Notable functions include:
  - `find_routes(data)`: Identifies popular routes and origins/destinations on a monthly and overall basis.
  - Two additional functions explore city migration rates based on origin and destination degrees.

* Companies module: With 10 functions, this module extracts extensive information about company income and popularity, self-explanatory by their function names.

This structured and modular approach to code design ensures that analysis tasks can be conducted efficiently, with results presented in a clear and organized manner.

</span>

