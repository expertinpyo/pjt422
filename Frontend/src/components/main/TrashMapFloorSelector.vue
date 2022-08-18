<template>
  <div class="floor-selector">
    <button
      v-for="floor in floors"
      :key="floor.id"
      @click="buttonClicked(floor)"
      class="floor-button"
      :class="{
        'btn-selected': currentFloor == floor.id,
        'btn-unselected': currentFloor != floor.id,
      }"
      type="button"
    >
      {{ floor.name }}F
      <span v-if="floor.notificationCount > 0" class="floor-notification badge">
        {{ floor.notificationCount }}
      </span>
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
  font-family: "Pretendard-Regular";
}
.floor-button {
  position: relative;
  width: 65px;
  height: 65px;
  border-radius: 100%;
  margin: 12px;
  font-size: 18px;
  border: 0;
}
.floor-button.btn-selected {
  border: 1px green solid;
}
.floor-notification {
  position: absolute !important;
  width: 30px;
  height: 25px;
  top: 0;
  right: 0;
  transform: translate(40%, -30%);
  background-color: white;
  border: 1.5px solid #646161;
  color: #bb2626;
  font-weight: 500;
}
.btn-selected {
  font-weight: bold;
}
</style>
