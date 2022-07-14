<template>
  <TrashMapFloorSelector />
  <TrashMap />
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
