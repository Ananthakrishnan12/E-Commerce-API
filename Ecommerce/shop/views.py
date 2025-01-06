from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer,ProductSerializer,OrderSerializer,PaymentSerializer
from .models import User,Product,Order,Payment
import jwt, datetime


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    
# Product List View
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({"message": "Product added successfully!"}, status=201)
        return Response(serializer.errors, status=400)
    

# Product Detail View
class ProductDetailView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found!"}, status=404)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found!"}, status=404)

        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product updated successfully!"})
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return Response({"message": "Product deleted successfully!"})
        except Product.DoesNotExist:
            return Response({"error": "Product not found!"}, status=404)
        
# Order Create View without authentication
class OrderCreateView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        # Check if the product exists
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return Response({"error": "Product not found!"}, status=404)

        # Calculate total price
        total_price = product.price * quantity

        # Create the order (no user field used)
        order = Order.objects.create(product=product, quantity=quantity, total_price=total_price)
        return Response({"message": "Order created successfully!", "order_id": order.id}, status=201)

    
# Order List View (without authentication)
class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()  # Fetch all orders, you can modify the filter as needed
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    
# Order Cancel View (without authentication)
class OrderCancelView(APIView):
    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            order.status = 'Cancelled'
            order.save()
            return Response({"message": "Order cancelled successfully!"})
        except Order.DoesNotExist:
            return Response({"error": "Order not found!"}, status=404)

# Mock Payment View
class MockPaymentView(APIView):
    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            payment = Payment.objects.create(order=order, amount=order.total_price, status='Completed')
            return Response({'payment_id': payment.id, 'status': payment.status}, status=201)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=404)