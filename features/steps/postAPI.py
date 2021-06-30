from behave import given, when, then
from asserts import assert_equal
import requests

from utilities.configurations import get_config
from resources.api_resources import ApiResources
from resources.posts_api import payload_resources, response_resources

config = get_config()


@given(u'a post that needs to be added')
def step_impl(context):
    context.body = payload_resources.posts_post_payload.body
    context.headers = payload_resources.posts_post_payload.headers
    context.expected_response = response_resources.posts_post_response


@when(u'we execute the posts API method')
def step_impl(context):
    context.response = requests.post(
        config["API"]["home"] + ApiResources.posts,
        json=context.body,
        headers=context.headers
    )


@then(u'the post is successfully added')
def step_impl(context):
    assert_equal(201, context.response.status_code,
                 f"Expected 201 but received {context.response.status_code}.")

    assert_equal(response_resources.posts_post_response, context.response.json(),
                 f"Expected {context.expected_response} but received {context.response.json()}.")

