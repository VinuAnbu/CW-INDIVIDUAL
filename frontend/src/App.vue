<template>
    <div class="background">
      <nav class="navbar navbar-expand-lg bg-light backgroundNav">
        <div class="container">
          <a class="navbar-brand" href="#"><h1>ORDER PRODUCTS</h1></a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto buttonsNav">
              <li class="nav-item">
                <button
                  type="button"
                  class="button"
                  data-bs-toggle="modal"
                  data-bs-target="#addOrderModal"
                >
                  Add Order
                </button>
              </li>
              <li class="nav-item">
                <button
                  type="button"
                  class="button"
                  data-bs-toggle="modal"
                  data-bs-target="#deleteOrderModal"
                >
                  Delete Order
                </button>
              </li>
              <li class="nav-item">
                <button
                  type="button"
                  class="button"
                  data-bs-toggle="modal"
                  data-bs-target="#updateOrderModal"
                >
                  Update Order
                </button>
              </li>
              <li class="nav-item">
                <button
                  type="button"
                  class="button"
                  data-bs-toggle="modal"
                  data-bs-target="#findOrderModal"
                >
                  Find Order
                </button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <div>
        <Modal modalId="findOrderModal" modalTitle="Find Order">
          <GetOrderInfo @order-info="handleOrderInfo" />
          <div v-if="receivedOrderInfo">
            <div class="container mt-4">
              <h2>Received Order Info</h2>
              <div class="card">
                <div class="card-body">
                  <p class="card-text">
                    <strong>Order ID:</strong>
                    {{ receivedOrderInfo.ID }}
                  </p>
                  <p class="card-text">
                    <strong>Customer Name:</strong>
                    {{ receivedOrderInfo.customer_name }}
                  </p>
                  <p class="card-text">
                    <strong>Product:</strong>
                    {{ receivedOrderInfo.product_name }}
                  </p>
                  <p class="card-text">
                    <strong>Quantity:</strong>
                    {{ receivedOrderInfo.quantity }}
                  </p>
                  <p class="card-text">
                    <strong>Order Date:</strong>
                    {{ receivedOrderInfo.order_date }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </Modal>
        <br />
        <div class="container pt-3">
          <Modal modalId="addOrderModal" modalTitle="Add New Order">
            <AddOrder />
          </Modal>
          <Modal modalId="deleteOrderModal" modalTitle="Delete Order">
            <DeleteOrder />
          </Modal>
          <Modal modalId="updateOrderModal" modalTitle="Update Order">
            <UpdateOrderForm />
          </Modal>
          <GetAllOrders />
        </div>
      </div>
    </div>
  </template>
  <script>
  import AddOrder from './components/AddOrder.vue';
  import DeleteOrder from './components/DeleteOrder.vue';
  import GetAllOrders from './components/GetAllOrders.vue';
  import GetOrderInfo from './components/GetOrderInfo.vue';
  import UpdateOrderForm from './components/UpdateOrderForm.vue';
  import Modal from './components/Modal.vue';
  
  
  export default {
    components: {
      AddOrder,
      DeleteOrder,
      GetAllOrders,
      GetOrderInfo,
      UpdateOrderForm,
      Modal,
    },

    data() {
      return {
        receivedOrderInfo: null,
      };
    },
    methods: {
      handleOrderInfo(orderInfo) {
        this.receivedOrderInfo = orderInfo;
      },
    },
  };
  </script>
  
  
  <style>
  .navButton {
    margin-right: 10px;
    margin-bottom: 10px;
  }
  * {
    font-family: "Times New Roman", Times, serif;
  }
  .buttonsNav {
    margin-left: 200px;
    align-content: center;
    justify-content: center;
    text-align: center;
  }
  .name {
    font-size: 30px;
  }
  .background {
    background-image: url("/path/to/your/background.jpg");
    height: 100vh;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;
  }
  .backgroundNav {
    background-color: #ececee;
  }
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
  