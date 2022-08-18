from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """
    This class define our pagination
    """
    
    page_size = 24
    page_size_query_param = 'page_size'
