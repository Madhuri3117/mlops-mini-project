# import mlflow
# print(mlflow.get_tracking_uri())

# from mlflow.tracking import MlflowClient

# client = MlflowClient()

# models = client.list_registered_models()
# for m in models:
#     print(m.name)

from mlflow.tracking import MlflowClient

client = MlflowClient()

models = client.search_registered_models()
print([m.name for m in models])
