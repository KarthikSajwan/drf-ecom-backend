from django.test import TestCase
from django.urls import reverse
from api.models import Order, User

class UserOrderTestCase(TestCase):
    def setUp(self):
        # Create test users
        user1 = User.objects.create_user(username='user1', password='testpass')
        user2 = User.objects.create_user(username='user2', password='testpass')

        # Create test orders for both users
        Order.objects.create(user=user1)
        Order.objects.create(user=user1)
        Order.objects.create(user=user2)
        Order.objects.create(user=user2)

    def test_user_order_endpoint_retrieves_only_authenticated_user_orders(self):
        # Log in user1
        user = User.objects.get(username='user1')
        self.client.force_login(user)

        # Call the API endpoint
        response = self.client.get(reverse('user-orders'))

        # Check if the response is successful
        assert response.status_code == 200

        # Parse the JSON response
        data = response.json()
        print(data)  # For debugging / verification

        # Ensure that only user1's orders are returned
        user_orders = Order.objects.filter(user=user)
        self.assertEqual(len(data), user_orders.count())

        # Validate that each order belongs to the logged-in user
        for order in data:
            self.assertEqual(order['user'], user.id)
