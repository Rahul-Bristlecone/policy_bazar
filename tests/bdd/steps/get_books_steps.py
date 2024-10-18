from behave import given, when, then
from BackEndAutomation.API import create_app

@given('the database contains books')
def book_in_db(context):
    context.app = create_app()
    context.client = context.app.test_client()

@when('the url is hit with get request along with the required endpoint')
def url_hit(context):
    context.response = context.client.get('/show')

@then('list of books is fetched and displayed')
def show_books(context):
    assert context.response.status_code == 200