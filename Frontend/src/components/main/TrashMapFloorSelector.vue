<template>
  <div class="floor-selector">
    <button
      v-for="floor in floors"
      :key="floor.id"
      @click="button_clicked(floor)"
      class="floor-button btn"
      :class="{
        'btn-primary': current_floor == floor.id,
        'btn-secondary': current_floor != floor.id,
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
  props: ["floors", "current_floor"],
  methods: {
    button_clicked(floor) {
      if (floor.id == this.current_floor) return;
      this.$emit("floor_changed", floor);
    },
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
