<img width="1494" alt="austin" src="https://user-images.githubusercontent.com/105242871/187056550-20ec57d7-a96d-4102-8f9a-f43c6462f2a5.png">

# Real-Time Traffic Incident Reports in Austin, Texas
by **Meredith Wang**

***

## Data Source
Data is acquire from [austintexas.gov](https://data.austintexas.gov/). This data set contains traffic incident information from the Austin-Travis County traffic reports RSS feed.

The dataset is updated every 5 minutes.

Incidents that are currently in the RSS feed have a status of "active" in this dataset. Incidents that are no longer appear in the feed have a status of "archived."

***

## Data Preparation
<details>
<summary> Convert Datatype</summary>

- Change `Published Data` to `datetime`
      ```
      df['Published Date'] = pd.to_datetime(df['Published Date'], infer_datetime_format=True)
      ```

- Set Index to Date
      ```
      df = df.set_index(df['Published Date'])
      ```
</details>

<details>
<summary> Missing Values</summary>

- Impute `Location` missing value by concatenating `Latitude` and `Longitude`
      ```
      df.Location.fillna("("+str(df.Latitude)+","+str(df.Longitude)+")", inplace = True)
      ```

- Drop NaNs in `Latitude` and `Longitude`
      ```
      df = df.dropna(subset = ['Latitude', 'Longitude'])
      ```
</details>

**Create `prepare.py` file for data cleaning functions**

***

## Data Context
As of Aug 27, 2022 there's 286460 incident reports in the dataset.

Keep in mind that this dataset is updated every 5 minutes. So the acquisition result would be different each time.

***

## Data Exploration
