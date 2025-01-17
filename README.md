# df-data-quality-ml

### Install

- **Install via setuptools**:
  ```sh
    python setup.py install
  ```


### Usage Examples

- **Apply DQ rules on a dataset via CLI**:
  ```sh
    dqml_app detect-anomalies --dataset_id "2" --env "dev"
  ```

  ##### If not installed
  ```sh
    python dqml_app detect-anomalies --dataset_id "2" --env "dev"
  ```

- **Apply DQ rules on a dataset via API**:
  ##### Start the API server
  ```sh
    python dqml_app/dqml_app_api.py
  ```
  ##### Invoke the API endpoint
  ```sh
    https://<host name with port number>/detect-anomalies/{dataset_id}
    https://<host name with port number>/detect-anomalies/2
  ```
  ##### Invoke the API from Swagger Docs interface
  ```sh
    https://<host name with port number>/docs

    /detect-anomalies/{dataset_id}
    /detect-anomalies/2
  ```

### Sample Input

  ##### Dataset (acct_positions_20241226.csv)
```
effective_date,account_id,asset_id,asset_value
2024-12-26,ACC1,1,35000
2024-12-26,ACC1,2,15000
2024-12-26,ACC2,2,12000
2024-12-26,ACC4,1,5000
```

### API Data (simulated)
These are metadata that would be captured via the DQ application UI and stored in a database.

  ##### datasets 
```
{
  "datasets": [
    {
      "dataset_id": "1",
      "catalog_ind": true,
      "file_delim": ",",
      "file_path": "APP_ROOT_DIR/data/source_data1.csv"
    },
    {
      "dataset_id": "2",
      "catalog_ind": true,
      "file_delim": ",",
      "file_path": "APP_ROOT_DIR/data/acct_positions_yyyymmdd.csv",
      "schedule_id": "2",
      "model_parameters": {
        "features": [
          {
            "column": "account_id",
            "variable_type": "category", 
            "variable_sub_type": "nominal", 
            "encoding": "frequency"
          },
          {
            "column": "asset_id",
            "variable_type": "category", 
            "variable_sub_type": "nominal", 
            "encoding": "one hot"
          },
          {
            "column": "asset_value",
            "variable_type": "numeric", 
            "variable_sub_type": "float", 
            "encoding": "numeric"
          }
        ],
        "hist_data_snapshots": [
          {
            "snapshot": "t-1d"
          },
          {
            "snapshot": "lme"
          }
        ], 
        "sample_size": 10000
      }
    },
    {
      "dataset_id": "3",
      "catalog_ind": true,
      "file_delim": ",",
      "file_path": "APP_ROOT_DIR/data/customer.csv"
    }
  ]
}
```

### Sample Output 

```
DQ check results for dataset 2
[
  {'rule_id': '1', 'result': True}, 
  {'rule_id': '2', 'result': True}, 
  {'rule_id': '3', 'result': False}
]
```
