import dagshub
import mlflow

mlflow.set_tracking_uri("https://dagshub.com/rohitgangurde112/mlop-mini-project.mlflow")
dagshub.init(repo_owner='rohitgangurde112', repo_name='mlop-mini-project', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)