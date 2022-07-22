<template>
  <div class="floor-selector">
    <button
      v-for="floor in floors"
      :key="floor.id"
      @click="buttonClicked(floor)"
      class="floor-button btn"
      :class="{
        'btn-primary': currentFloor == floor.id,
        'btn-secondary': currentFloor != floor.id,
      }"
      type="button"
    >
      {{ floor.name }}F
    </button>
  </div>
</template>

<script>
export default {
  name: "TrashMapFloorSelector",
  props: ["floors", "currentFloor"],
  methods: {
    buttonClicked(floor) {
      if (floor.id == this.currentFloor) return;
      this.$emit("floorChanged", floor);
    },
  },
};
</script>

<style scoped>
.floor-selector {
  justify-content: center;
}
.floor-button {
  width: 80px;
  margin-bottom: 10px;
}
</style>
