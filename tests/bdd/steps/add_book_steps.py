from behave import given, when, then
from BackEndAutomation.API import create_app


# step definition of add book feature
@given('a json payload is provided with book data')
def payload_step(context):
    context.app = create_app()
    context.client = context.app.test_client()


@when('the url is hit with post request and required endpoint')
def url_step(context):
    context.response = context.client.post("\add", data={"id": 31, "name": "satnam"})


@then('book is added to the db')
def book_in_db_step(context):
    assert context.response.status_code == 200
