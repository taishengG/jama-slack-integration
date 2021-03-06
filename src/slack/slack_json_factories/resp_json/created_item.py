import json

"""Returns url to access created item

This function packages the response from Jama after and item
has either been created or attempted to be created. If there is an error
in the post request to the Jama instance, then this function will notify the
user. If the post request was successful, then the function will return the
newly created url to the user.

Attributes:
    None
"""


def resp_json(payload_to_format, project_id):
    """Packages a response to send to slack

    Function takes in a JSON object, and uses the following format at
    the following link:
        https://api.slack.com/docs/messages#composing_messages

    Returns: 
        created JSON object, then is sent back to Slack.
    
    Raises:
        Exception:
            If object was not created, then excpetion is raised and
            and error message is sent to the user
    """
    try:
        url_to_new_item = "https://capstone-test.jamacloud.com/perspective.req#/items/{item_id}?projectId={prj_id}".format(
            item_id=str(payload_to_format["meta"]["id"]), prj_id=project_id
        )

        return {
            "text": payload_to_format["meta"]["status"],
            "attachments": [
                {
                    "title": "New Item ID",
                    "text": payload_to_format["meta"]["id"]  # ID from Jama JSON
                },
                {
                    "title": "Url to new item",
                    "text": url_to_new_item
                }
            ]
        }

    except Exception as err:
        print(err)
        return {
            "text": "Oh no, there was an error creating the object",
            "attachments": [
                    {
                        "text": "Your error may be your inputs or item type\n\
                        example input format: /jamaconnect create: project=49 | name=project name | ...\n\
                        - or the new item may conflict with the intended item list - \n\
                        Hint: You can always create a text item, then convert later"
                    }
            ]
        }
