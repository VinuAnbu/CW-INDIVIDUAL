import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from api.models import Customer, Product, Order

def test_api_view(request):
    return JsonResponse({"message": "Good response!"})

def get_all_orders(request):
    orders = Order.objects.all()

    order_list = []
    for order in orders:
        order_dict = {
            "id": order.id,
            "customer": order.customer.name,
            "product": order.product.name,
            "quantity": order.quantity,
            "order_date": order.order_date,
            "is_fulfilled": order.is_fulfilled,
        }
        order_list.append(order_dict)

    return JsonResponse(order_list, safe=False)

def get_customer_orders(request, customer_id):
    try:
        customer_orders = Order.objects.filter(customer_id=customer_id)
        order_list = [
            {
                "id": order.id,
                "product": order.product.name,
                "quantity": order.quantity,
                "order_date": order.order_date,
                "is_fulfilled": order.is_fulfilled,
            }
            for order in customer_orders
        ]
        return JsonResponse(order_list, safe=False)
    except Customer.DoesNotExist:
        return JsonResponse({"Error": "Customer not found"}, status=404)

@csrf_exempt
@require_POST
def add_order(request):
    try:
        order_data = json.loads(request.body)

        customer_name = order_data.get("customer_name")
        product_name = order_data.get("product_name")
        quantity = order_data.get("quantity")
        order_date = order_data.get("order_date")
        is_fulfilled = order_data.get("is_fulfilled", False)

        if customer_name and product_name and quantity:
            # Get the Customer and Product objects by their names
            try:
                customer = Customer.objects.get(name=customer_name)
            except Customer.DoesNotExist:
                return JsonResponse({"message": "Customer not found"}, status=404)

            try:
                product = Product.objects.get(name=product_name)
            except Product.DoesNotExist:
                return JsonResponse({"message": "Product not found"}, status=404)

            # Create an Order instance
            order = Order(
                customer=customer,
                product=product,
                quantity=quantity,
                order_date=order_date,
                is_fulfilled=is_fulfilled,
            )
            order.save()
            return JsonResponse({"message": "Order added successfully"})
        else:
            return JsonResponse({"message": "Order not added. Missing required fields."}, status=400)

    except json.JSONDecodeError as e:
        return JsonResponse({"message": f"Invalid JSON data: {str(e)}"}, status=400)

    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)

@csrf_exempt
def delete_order(request, order_id):
    if request.method == "DELETE":
        try:
            order = Order.objects.get(id=order_id)
            order.delete()
            return JsonResponse({"message": "Order deleted successfully"})
        except Order.DoesNotExist:
            return JsonResponse({"message": "Order not found"}, status=404)

@csrf_exempt
def update_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        if request.method == "PUT":
            # Handle PUT request to update the order
            data = json.loads(request.body)
            new_customer_name = data.get("customer_name")
            new_product_name = data.get("product_name")
            new_quantity = data.get("quantity")
            new_order_date = data.get("order_date")
            new_is_fulfilled = data.get("is_fulfilled")

            if new_customer_name and new_product_name and new_quantity:
                # Get the new Customer and Product objects by their names
                try:
                    new_customer = Customer.objects.get(name=new_customer_name)
                except Customer.DoesNotExist:
                    return JsonResponse({"message": "Customer not found"}, status=404)

                try:
                    new_product = Product.objects.get(name=new_product_name)
                except Product.DoesNotExist:
                    return JsonResponse({"message": "Product not found"}, status=404)

                # Update the order
                order.customer = new_customer
                order.product = new_product
                order.quantity = new_quantity
                order.order_date = new_order_date
                order.is_fulfilled = new_is_fulfilled
                order.save()
                return JsonResponse({"message": "Order updated successfully"})
            else:
                return JsonResponse({"error": "Required fields are missing"}, status=400)
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
