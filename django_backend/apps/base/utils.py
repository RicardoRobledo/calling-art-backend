from rest_framework.response import Response


__author__ = 'Ricardo'
__version__ = '0.1'


# ---------------------------------------------
#                format response
# ---------------------------------------------


def format_response(message:dict, status:int) -> Response:
    """
    This function gives format to the response

    Args:
        message (dict): contains our message to show
        status (int): contains our status to reponse

    Returns:
        Our response object
    """

    return Response(message, status=status)
