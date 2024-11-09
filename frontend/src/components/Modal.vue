<!-- ReusableModal.vue -->
<template>
  <div
    class="modal fade"
    :id="modalId"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">
            {{ modalTitle }}
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <slot></slot>
          <!-- This is where the content from child components will be placed -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    modalId: String, // Unique ID for the modal
    modalTitle: String, // Title for the modal
  },
};
</script>
