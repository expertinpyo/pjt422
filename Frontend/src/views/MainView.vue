<template>
  <div class="trash-map-container">
    <TrashMapFloorSelector />
    <TrashMap />
  </div>
</template>

<script>
// @ is an alias to /src
import TrashMapFloorSelector from "@/components/main/TrashMapFloorSelector.vue";
import TrashMap from "@/components/main/TrashMap.vue";

export default {
  name: "MainView",
  components: {
    TrashMapFloorSelector,
    TrashMap,
  },
};
</script>

<style scoped>
.trash-map-container {
  display: flex;
}
</style>
