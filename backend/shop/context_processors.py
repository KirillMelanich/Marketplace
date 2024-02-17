from .models import Category


def categories(request):
    """
    Retrieves all categories that have no parent category.

    Args:
         request: The HTTP request object.
    Returns:
        A dictionary containing the categories that have no parent category.
    """
    no_parent_categories = Category.objects.filter(parent=None)
    return {"categories": no_parent_categories}
