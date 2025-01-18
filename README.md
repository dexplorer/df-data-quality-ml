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
2024-12-26,ACC1,1,-35000
2024-12-26,ACC1,2,-15000
2024-12-26,ACC2,2,10000
2024-12-26,ACC4,1,-5000
2024-12-26,ACC5,1,-5000
2024-12-26,ACC6,1,-5000
2024-12-26,ACC7,1,-5000
2024-12-26,ACC8,1,-5000
2024-12-26,ACC9,1,-5000
```

  ##### Dataset (acct_positions_20241225.csv)
```
effective_date,account_id,asset_id,asset_value
2024-12-25,ACC1,1,34000
2024-12-25,ACC1,2,14500
2024-12-25,ACC2,2,13000
2024-12-25,ACC3,1,10000
```

  ##### Dataset (acct_positions_20241130.csv)
```
effective_date,account_id,asset_id,asset_value
2024-11-30,ACC1,1,30000
2024-11-30,ACC2,2,15000
```

### API Data (simulated)
These are metadata that would be captured via the DQ application UI and stored in a database.

  ##### datasets 
```
{
  "datasets": [
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
    }
  ]
}
```

### Sample Output 

#### Raw data
```
  effective_date account_id asset_id asset_value
0     2024-12-26       ACC1        1      -35000
1     2024-12-26       ACC1        2      -15000
2     2024-12-26       ACC2        2       10000
3     2024-12-26       ACC4        1       -5000
4     2024-12-26       ACC5        1       -5000
5     2024-12-26       ACC6        1       -5000
6     2024-12-26       ACC7        1       -5000
7     2024-12-26       ACC8        1       -5000
8     2024-12-26       ACC9        1       -5000
  effective_date account_id asset_id asset_value
0     2024-12-25       ACC1        1       34000
1     2024-12-25       ACC1        2       14500
2     2024-12-25       ACC2        2       13000
3     2024-12-25       ACC3        1       10000
4     2024-11-30       ACC1        1       30000
5     2024-11-30       ACC2        2       15000
```

#### Features
There are 15 samples/observations and 4 features in the data.

Features are encoded into numeric values.
account_id - Frequency encoding
asset_id - One hot encoding
asset_value - Normalized by diving by max asset value

```
    account_id  asset_id_0  asset_id_1  asset_value
0     0.333333         1.0         0.0    -1.029412
1     0.333333         0.0         1.0    -0.441176
2     0.200000         0.0         1.0     0.294118
3     0.066667         1.0         0.0    -0.147059
4     0.066667         1.0         0.0    -0.147059
5     0.066667         1.0         0.0    -0.147059
6     0.066667         1.0         0.0    -0.147059
7     0.066667         1.0         0.0    -0.147059
8     0.066667         1.0         0.0    -0.147059
9     0.333333         1.0         0.0     1.000000
10    0.333333         0.0         1.0     0.426471
11    0.200000         0.0         1.0     0.382353
12    0.066667         1.0         0.0     0.294118
13    0.333333         1.0         0.0     0.882353
14    0.200000         0.0         1.0     0.441176
```

#### Target Labels
'1' - Current day data

'0' - Prior day data

```
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
```

#### Data (Features) for prediction
Test data for explainer

```
   account_id  asset_id_0  asset_id_1  asset_value
0    0.333333         1.0         0.0    -1.029412
1    0.333333         0.0         1.0    -0.441176
2    0.200000         0.0         1.0     0.294118
3    0.066667         1.0         0.0    -0.147059
4    0.066667         1.0         0.0    -0.147059
5    0.066667         1.0         0.0    -0.147059
6    0.066667         1.0         0.0    -0.147059
7    0.066667         1.0         0.0    -0.147059
8    0.066667         1.0         0.0    -0.147059
```

#### SHAP values
These SHAP values are output by a Tree Explainer. 
Each column represent a feature. There are 4 features.

```
[[-0.19850235  0.          0.          0.8979624 ]
 [-0.19850235  0.          0.          0.8979624 ]
 [-0.19850235  0.          0.         -1.0153805 ]
 [ 0.21120496  0.          0.          0.8979624 ]
 [ 0.21120496  0.          0.          0.8979624 ]
 [ 0.21120496  0.          0.          0.8979624 ]
 [ 0.21120496  0.          0.          0.8979624 ]
 [ 0.21120496  0.          0.          0.8979624 ]
 [ 0.21120496  0.          0.          0.8979624 ]]
```

#### SHAP value plots

##### Summary Plot (All Samples)
![dataset_id_2_shap_summary](https://github.com/user-attachments/assets/a8d117ca-6d6a-4938-a389-564d596121d6)

##### Waterfall Plot (1 Sample) 
![dataset_id_2_shap_waterfall](https://github.com/user-attachments/assets/a8d117ca-6d6a-4938-a389-564d596121d6)

#### Feature scores
Feature importance scores are the average (mean) of absolute SHAP values for the feature/column.

```
{
  "results": [
    {
      "feature_name": "asset_value",
      "feature_importance": 0.9110089540481567
    },
    {
      "feature_name": "account_id",
      "feature_importance": 0.20697076618671417
    },
    {
      "feature_name": "asset_id_0",
      "feature_importance": 0.0
    },
    {
      "feature_name": "asset_id_1",
      "feature_importance": 0.0
    }
  ]
}
```
