<template>
  <div class="floor-selector">
    <button
      v-for="floor of floors"
      :key="floor"
      class="floor-button btn btn-secondary"
      type="button"
    >
      {{ floor }}
    </button>
  </div>
</template>

<script>
export default {
  name: "TrashMapFloorSelector",
  data() {
    return {
      floors: [],
    };
  },
  mounted() {
    // TODO: 층수 불러오기 기능
    this.floors = ["B1", "1", "2", "3"];
  },
};
</script>

<style scoped>
.floor-selector {
  width: 80px;
  justify-content: center;
}
.floor-button {
  width: 60px;
  margin-bottom: 10px;
}
</style>
