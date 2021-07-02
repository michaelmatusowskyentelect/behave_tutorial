from behave import given, when, then
from asserts import assert_equal
import requests

from utilities.configurations import get_config
from resources.api_resources import ApiResources
from resources.posts_api import response_resources

config = get_config()


@given(u'a post id')
def step_impl(context):
    context.id = "1"
    context.expected_response = response_resources.posts_get_response


@when(u'we execute the GET API method')
def step_impl(context):
    context.response = requests.get(
        config["API"]["home"]+ApiResources.posts+"/"+context.id
    )


@then(u'the post is successfully received')
def step_impl(context):
    assert_equal(200, context.response.status_code,
                 f"Expected response 200 received {context.response.status_code}.")

    assert_equal(context.expected_response, context.response.json(),
                 f"Expected response {context.expected_response} but received {context.response.json()}.")
