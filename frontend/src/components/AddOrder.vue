<template>
    <div class="container">
      <form @submit.prevent="addOrder">
        <div class="mb-3">
          <label for="customer_name" class="form-label">Customer Name:</label>
          <input
            type="text"
            id="customer_name"
            v-model="customer_name"
            class="form-control"
            required
          />     
        </div>
  
        <div class="mb-3">
          <label for="product_name" class="form-label">Product Name:</label>
          <input
            type="text"
            id="product_name"
            v-model="product_name"
            class="form-control"
            required
          />
        </div>
  
        <div class="mb-3">
          <label for="quantity" class="form-label">Quantity:</label>
          <input
            type="number"
            id="quantity"
            v-model="quantity"
            class="form-control"
            required
          />
        </div>
  
        <div class="mb-3">
          <label for="order_date" class="form-label">Order Date:</label>
          <input
            type="date"
            id="order_date"
            v-model="order_date"
            class="form-control"
            required
          />
        </div>
  
        <button type="submit" class="button">Add Order</button>
      </form>
  
      <div v-if="successMessage" class="alert alert-success mt-3">
        <p>{{ successMessage }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        customer_name: "",
        product_name: "",
        quantity: null,
        order_date: "",
        successMessage: "",
      };
    },
    methods: {
      addOrder() {
        const orderData = {
          customer_name: this.customer_name,
          product_name: this.product_name,
          quantity: this.quantity,
          order_date: this.order_date,
        };
  
        // Make a POST request to your Django backend API
        fetch("http://localhost:8000/api/addOrder", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(orderData),
        })
          .then((response) => {
            if (response.ok) {
              this.successMessage = "Order added successfully!";
              setTimeout(() => {
                this.successMessage = ""; // Clear success message after 2 seconds
              }, 2000);
              return response.json();
            } else {
              throw new Error("Failed to add order");
            }
          })
          .then((data) => {
            console.log(data.message);
          })
          .catch((error) => {
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
  