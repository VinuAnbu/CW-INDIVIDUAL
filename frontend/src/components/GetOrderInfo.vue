<template>
    <div class="container">
      <div class="mb-3">
        <label for="orderId" class="form-label">Enter Order ID:</label>
        <input type="text" id="order_id" v-model="orderId" class="form-control" />
      </div>
      <br />
      <button @click="getOrderInfo" class="button">Get Order Info</button>
  
      <div class="mt-3" v-if="error">
        <div class="alert alert-danger">{{ error }}</div>
      </div>
  
      <div v-if="orderInfo" class="mt-3">
        <h4>Order Details</h4>
        <p><strong>Order ID:</strong> {{ orderInfo.id }}</p>
        <p><strong>Customer Name:</strong> {{ orderInfo.customer_name }}</p>
        <p><strong>Product Name:</strong> {{ orderInfo.product_name }}</p>
        <p><strong>Quantity:</strong> {{ orderInfo.quantity }}</p>
        <p><strong>Status:</strong> {{ orderInfo.status }}</p>
        <p><strong>Order Date:</strong> {{ orderInfo.order_date }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        orderId: "",   // The order ID entered by the user
        error: "",     // Error message if any error occurs
        orderInfo: null, // Stores the order information once fetched
      };
    },
    methods: {
      async getOrderInfo() {
        this.error = ""; // Reset the error message
        this.orderInfo = null; // Clear any previously displayed order info
  
        try {
          // Fetch order information from the API based on the provided orderId
          const response = await fetch(
            `http://localhost:8000/api/order/${this.orderId}`
          );
          if (response.ok) {
            const orderInfo = await response.json();
            this.orderInfo = orderInfo; // Set the orderInfo if successful
          } else if (response.status === 404) {
            this.error = "Order not found. Please enter a valid Order ID.";
          } else {
            this.error = "Failed to fetch order information. Please try again.";
          }
        } catch (error) {
          this.error = "An error occurred. Please try again.";
        }
      },
    },
  };
  </script>
  
  <style>
  .button {
    background-color: #a79d88;
    border-radius: 10px;
    border-width: 0;
    display: inline-block;
    font-weight: 400;
    text-align: center;
    border: 1px solid transparent;
    padding: 0.375rem 0.75rem;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: 0.25rem;
    color: #fff;
    margin-right: 10px;
  }
  </style>
  