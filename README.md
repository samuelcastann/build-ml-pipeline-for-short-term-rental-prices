# Build an ML Pipeline for Short-Term Rental Prices in NYC
You are working for a property management company renting rooms and properties for short periods of 
time on various rental platforms. You need to estimate the typical price for a given property based 
on the price of similar properties. Your company receives new data in bulk every week. The model needs 
to be retrained with the same cadence, necessitating an end-to-end pipeline that can be reused.

<br />

### You can look at my public W&B project [here](https://wandb.ai/samuel-castan96/nyc_airbnb/overview?workspace=user-samuel-castan96) 

<br />


### [Link](https://github.com/samuelcastann/build-ml-pipeline-for-short-term-rental-prices/tree/1.0.3) for the GitHub repo

<br />

### To run the latest version (1.0.3) please use the following command on your terminal <br />

```
mlflow run https://github.com/samuelcastann/build-ml-pipeline-for-short-term-rental-prices.git -v 1.0.4 -P hydra_options="etl.sample='sample2.csv'"
```