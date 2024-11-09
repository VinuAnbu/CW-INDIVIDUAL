<template>
    <div class="container">
      <form @submit.prevent="fetchOldOrderInfo" class="mb-3">
        <label for="orderId" class="form-label">Enter Order ID to Update:</label>
        <input
          type="text"
          id="order_id"
          v-model="order_id"
          class="form-control"
        />
        <br />
        <button type="submit" class="button">Find Order</button>
      </form>
  
      <div v-if="errorMessage" class="alert alert-danger mt-3">
        <p>{{ errorMessage }}</p>
      </div>
  
      <div v-if="old_order_info">
        <h3>Old Order Information:</h3>
  
        <form @submit.prevent="updateOrderForm" class="mt-3">
          <div class="mb-3">
            <label for="customer_name" class="form-label">Customer Name:</label>
            <input
              type="text"
              id="customer_name"
              v-model="old_order_info.customer_name"
              class="form-control"
            />
          </div>
  
          <div class="mb-3">
            <label for="product_name" class="form-label">Product Name:</label>
            <input
              type="text"
              id="product_name"
              v-model="old_order_info.product_name"
              class="form-control"
            />
          </div>
  
          <div class="mb-3">
            <label for="order_date" class="form-label">Order Date:</label>
            <input
              type="date"
              id="order_date"
              v-model="old_order_info.order_date"
              class="form-control"
            />
          </div>
  
          <div class="mb-3">
            <label for="order_status" class="form-label">Order Status:</label>
            <select
              id="order_status"
              v-model="old_order_info.order_status"
              class="form-control"
            >
              <option value="Pending">Pending</option>
              <option value="Shipped">Shipped</option>
              <option value="Delivered">Delivered</option>
              <option value="Cancelled">Cancelled</option>
            </select>
          </div>
          <br />
          <button type="submit" class="button">Update Order</button>
        </form>
        <div v-if="successMessage" class="alert alert-success mt-3">
          <p>{{ successMessage }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        order_id: "",
        old_order_info: null,
        errorMessage: "",
        successMessage: "",
      };
    },
    methods: {
      async fetchOldOrderInfo() {
        if (!this.order_id) {
          this.errorMessage = "";
          this.old_order_info = null;
          return;
        }
        try {
          const response = await fetch(
            `http://localhost:8000/api/order/${this.order_id}`
          );
          if (response.ok) {
            const data = await response.json();
            this.old_order_info = data;
            this.errorMessage = "";
          } else {
            this.errorMessage = "Order not found. Please enter a valid Order ID.";
            this.old_order_info = null;
            console.error("Failed to fetch old order information");
          }
        } catch (error) {
          console.error(error);
          this.errorMessage = "An error occurred. Please try again.";
        }
      },
      async updateOrderForm() {
        if (!this.order_id || !this.old_order_info) {
          return;
        }
        try {
          const response = await fetch(
            `http://localhost:8000/api/updateOrder/${this.order_id}`,
            {
              method: "PUT",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(this.old_order_info),
            }
          );
          if (response.ok) {
            console.log("Order updated successfully");
            this.successMessage = "Order updated successfully!";
            setTimeout(() => {
              this.successMessage = ""; // Clear success message after 5 seconds
              this.order_id = "";  // Clear order id
              this.old_order_info = null; // Clear form data
            }, 2000);
          } else {
            this.errorMessage = "Failed to update order. Please try again.";
            console.error("Failed to update order");
          }
        } catch (error) {
          console.error(error);
          this.errorMessage = "An error occurred. Please try again.";
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
  