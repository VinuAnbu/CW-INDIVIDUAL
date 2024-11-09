<template>
  <div class="container">
    <div class="order-card">
      <h4>{{ order.product_name }}</h4>
      <p><strong>Customer Name:</strong> {{ order.customer_name }}</p>
      <p><strong>Quantity:</strong> {{ order.quantity }}</p>
      <p><strong>Order Date:</strong> {{ order.order_date }}</p>
      <button @click="$emit('delete-order')" class="button">Delete Order</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    order: Object,
  },
};
</script>

<style scoped>
.container {
  margin-top: 20px;
}

.order-card {
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #f9f9f9;
  margin: 10px;
}

.order-card h4 {
  font-size: 1.25rem;
  margin-bottom: 10px;
}

.order-card p {
  font-size: 1rem;
  margin-bottom: 5px;
}

.button {
  background-color: #a79d88;
  border-radius: 10px;
  padding: 0.375rem 0.75rem;
  color: white;
  font-size: 1rem;
  border: none;
  cursor: pointer;
}

.button:hover {
  background-color: #8a7d5b;
}
</style>
