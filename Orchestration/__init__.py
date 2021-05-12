import azure.functions as func
import azure.durable_functions as df
import logging


def orchestrator_function(context: df.DurableOrchestrationContext):
    url = "https://fortesting.azurewebsites.net/api/Function1?code=caATd9U/wemV9vBy7ySFHfiEJCfQr0QZYzCdzGBHvIkWapwdjvjV1g=="

    result = yield context.call_activity('Activity', url)
    return [result]


main = df.Orchestrator.create(orchestrator_function)
