<template>
    <form @submit.prevent="deleteOrder">
      <div class="mb-3">
        <label for="order_id" class="form-label">Enter Order ID:</label>
        <input
          type="number"
          id="order_id"
          v-model="order_id"
          class="form-control"
          required
        />
      </div>
  
      <button type="submit" class="button">Delete Order</button>
  
      <div class="mt-3" v-if="errorMessage">
        <div class="alert alert-danger">{{ errorMessage }}</div>
      </div>
    </form>
  </template>
  
  <script>
  export default {
    data() {
      return { order_id: "", errorMessage: "" };
    },
    methods: {
      async deleteOrder() {
        this.errorMessage = ""; // Reset the error message
        if (!this.order_id) {
          return;
        }
  
        // Send a DELETE request to your Django backend
        fetch(`http://localhost:8000/api/deleteOrder/${this.order_id}`, {
          method: "DELETE",
        })
          .then((response) => {
            if (response.ok) {
              // Handle a successful deletion, e.g., show a success message
              console.log("Order deleted successfully");
              this.errorMessage = "Order deleted successfully";
            } else if (response.status === 404) {
              // Handle a 404 error, which indicates that the order with the given ID was not found
              this.errorMessage = "Order not found. Please enter a valid Order ID.";
            } else {
              // Handle other error responses, e.g., show a general error message
              this.errorMessage = "Failed to delete order.";
            }
          })
          .catch((error) => {
            // Handle any errors, e.g., show an error message
            this.errorMessage = "An error occurred. Please try again.";
            console.error(error.message);
          });
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
  