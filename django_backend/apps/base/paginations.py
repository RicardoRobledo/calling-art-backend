from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """
    This class define our pagination
    """
    
    page_size = 25
    page_size_query_param = 'page_size'
