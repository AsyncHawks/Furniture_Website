from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.models.product import Product
from shop.models.collections import Collection
from shop.models.category import Category
from shop.models.buy_together import BuyTogether


def _product_to_dict(prod):
    # helper to shape a product into the JSON structure you showed
    # categories -> names of collections
    categories = [c.name for c in prod.collections.all()]

    # images -> main image + any ProductImage urls
    images = []
    try:
        if prod.image and hasattr(prod.image, 'url'):
            images.append(prod.image.url)
    except Exception:
        pass
    # related name for ProductImage is `product_images`
    for pi in getattr(prod, 'product_images', prod.product_images).all():
        try:
            if pi.image and hasattr(pi.image, 'url'):
                images.append(pi.image.url)
        except Exception:
            continue

    # variants
    variants = []
    for v in prod.variants.all():
        variants.append({
            'id': v.id,
            'title': v.title,
            'price': v.price,
        })

    # buyTogether: list of recommended products (simple serialization)
    buy_together = []
    for bt in BuyTogether.objects.filter(product=prod):
        rp = bt.recommended_product
        buy_together.append({
            'id': rp.id,
            'title': rp.title,
            'price': rp.price,
            'images': [img.image.url for img in rp.product_images.all() if getattr(img.image, 'url', None)],
            'variants': [{'id': v.id, 'title': v.title, 'price': v.price} for v in rp.variants.all()]
        })

    product_dict = {
        'id': prod.id,
        'title': prod.title,
        'price': prod.price,
        'slug': prod.slug,
        'categories': categories,
        'generalCategory': prod.general_category.name if prod.general_category else None,
        'vendor': prod.vendor.name if prod.vendor else None,
        'description': prod.description,
        'features': prod.features,
        'images': images,
        'freeShipping': prod.free_shipping,
        'available': prod.available_in,
        'sold': prod.sold,
        'itemsInStock': prod.items_in_stock,
        'createdAt': prod.created_at.date().isoformat() if prod.created_at else None,
        'variants': variants,
        'buyTogether': buy_together,
    }

    return product_dict


@api_view(['GET'])
def products_by_category(request, category_id):
    products = Product.objects.filter(general_category__id=category_id)
    data = [_product_to_dict(p) for p in products]
    return Response(data)


@api_view(['GET'])
def products_by_vendor(request, vendor_id):
    products = Product.objects.filter(vendor__id=vendor_id)
    data = [_product_to_dict(p) for p in products]
    return Response(data)


@api_view(['GET'])
def products_in_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    products = collection.products.all()  # Get all products in this collection
    data = [_product_to_dict(p) for p in products]
    return Response(data)


@api_view(['GET'])
def collections_list(request):
    """Return collections derived from Category entries.

    Each item includes `title`, `link`, and an optional `image`.
    The `link` points to the products-by-category API route.
    """
    collections = []
    for cat in Category.objects.all():
        # pick an image from first product in this category if available
        image_url = None
        prod = Product.objects.filter(general_category=cat).first()
        if prod:
            try:
                if prod.image and hasattr(prod.image, 'url'):
                    image_url = prod.image.url
                else:
                    pi = prod.product_images.first()
                    if pi and getattr(pi.image, 'url', None):
                        image_url = pi.image.url
            except Exception:
                image_url = None

        collections.append({
            'id': cat.id,
            'title': cat.name,
            'link': f"/api/products/category/{cat.id}/",
            'image': image_url,
        })

    return Response(collections)


@api_view(['GET'])
def product_detail(request, product_slug):
    # Fetch the product by its slug
    product = Product.objects.get(slug=product_slug)

    # Related products: all products in the same general_category (exclude self)
    if product.general_category:
        related_products_qs = Product.objects.filter(general_category=product.general_category).exclude(id=product.id)
    else:
        related_products_qs = Product.objects.none()

    product_data = _product_to_dict(product)
    related_products = [_product_to_dict(p) for p in related_products_qs]

    return Response({
        'product': product_data,
        'relatedProducts': related_products
    })
