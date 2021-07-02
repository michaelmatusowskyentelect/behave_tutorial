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


@given(u'a post with {user_id:d} {title} and {body}')
def step_impl(context, user_id, title, body):
    context.body = {
        "userId": user_id,
        "title": title,
        "body": body
    }
    context.headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    context.expected_response = {
        "userId": user_id,
        "title": title,
        "body": body,
        "id": 101
    }


@when(u'we execute the POST API method')
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

    assert_equal(context.expected_response, context.response.json(),
                 f"Expected {context.expected_response} but received {context.response.json()}.")
