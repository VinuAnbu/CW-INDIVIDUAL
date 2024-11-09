<template>
    <div class="allOrders">
      <h2>All Orders</h2>
      <div v-if="orders.length > 0">
        <div class="row">
          <div class="col-md-4" v-for="order in orders" :key="order.id">
            <!-- Use the OrderCard component to display each order -->
            <order-card-vue
              :order="order"
              @delete-order="deleteOrder(order.id)"
            />
          </div>
        </div>
      </div>
      <div v-else>
        <p>No orders found.</p>
      </div>
    </div>
  </template>
  
  <script>
  import OrderCardVue from "./OrderCard.vue"; // Component to display individual orders
  
  export default {
    data() {
      return {
        orders: [], // To store the list of orders
      };
    },
    mounted() {
      // Fetch all orders from the API when the component is mounted
      this.fetchAllOrders();
    },
    components: {
      OrderCardVue, // Register the OrderCard component
    },
    methods: {
      async fetchAllOrders() {
        try {
          const response = await fetch(`http://localhost:8000/api/allOrders`);
          if (response.ok) {
            const data = await response.json();
            this.orders = data;
          } else {
            console.error("Failed to fetch orders");
          }
        } catch (error) {
          console.error(error);
        }
      },
      async deleteOrder(orderId) {
        try {
          const response = await fetch(
            `http://localhost:8000/api/deleteOrder/${orderId}`,
            {
              method: "DELETE",
            }
          );
  
          if (response.ok) {
            this.orders = this.orders.filter((order) => order.id !== orderId);
            console.log("Order deleted successfully");
          } else if (response.status === 404) {
            console.error("Order not found. Please enter a valid Order ID.");
          } else {
            console.error("Failed to delete order.");
          }
        } catch (error) {
          console.error(error);
        }
      },
    },
  };
  </script>
  
  <style>
  .allOrders {
    margin-bottom: 300px;
  }
  </style>
  