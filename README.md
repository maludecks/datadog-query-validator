# Datadog query validator
Python script to validate a monitor query through [Datadog API](https://docs.datadoghq.com/) using [Datadog Python Library](https://github.com/DataDog/datadogpy).

## Installing
In order to run a validation you will need a Datadog API key and an Application key from your Datadog account. See [Datadog documentation](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys) for more information about how to get them.

Then install [Datadog Python Library](https://github.com/DataDog/datadogpy):
```
pip install datadog
```

Create a `config.json` file from the template:
```
cp config.dist.json config.json
```

Replace the placeholders in the `config.json` with your API and Application key, and add the query information you want to validate.

## Running
With the `config.json` and the installation ready, in your terminal, run the following command:
```
python validate.py
```
