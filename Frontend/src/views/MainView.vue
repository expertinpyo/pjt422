<template>
  <div class="trash-map-container">
    <TrashMapFloorSelector
      :floors="floors"
      :current_floor="current_floor"
      @floor_changed="change_floor"
    />
    <TrashMap :floor="floors[current_floor]" :width="800" :height="600" />
  </div>
</template>

<script>
import TrashMapFloorSelector from "@/components/main/TrashMapFloorSelector.vue";
import TrashMap from "@/components/main/TrashMap.vue";

export default {
  name: "MainView",
  components: {
    TrashMapFloorSelector,
    TrashMap,
  },
  data() {
    return {
      current_floor: 0,
      floors: [
        {
          id: 0,
          name: "B1",
          src: require("@/assets/test_map_b1.png"),
          width: 860,
          height: 310,
          trash_bins: [
            {
              name: "name1",
              color: "#AA0000",
              x: 200,
              y: 200,
              size: 20,
            },
            {
              name: "name2",
              color: "#00AA00",
              x: 222,
              y: 200,
              size: 20,
            },
            {
              name: "name3",
              color: "#0000AA",
              x: 244,
              y: 200,
              size: 20,
            },
          ],
        },
        {
          id: 1,
          name: "1",
          src: require("@/assets/test_map_1.png"),
          width: 860,
          height: 310,
          trash_bins: [
            {
              name: "name1",
              color: "#AAAA00",
              x: 200,
              y: 200,
              size: 20,
            },
            {
              name: "name2",
              color: "#00AAAA",
              x: 222,
              y: 200,
              size: 20,
            },
            {
              name: "name3",
              color: "#AA00AA",
              x: 244,
              y: 200,
              size: 20,
            },
          ],
        },
        {
          id: 2,
          name: "2",
          src: require("@/assets/test_map_2.png"),
          width: 860,
          height: 310,
          trash_bins: [
            {
              name: "name1",
              color: "#0000AA",
              x: 200,
              y: 200,
              size: 20,
            },
            {
              name: "name2",
              color: "#AA0000",
              x: 222,
              y: 200,
              size: 20,
            },
            {
              name: "name3",
              color: "#00AA00",
              x: 244,
              y: 200,
              size: 20,
            },
          ],
        },
        {
          id: 3,
          name: "3",
          src: require("@/assets/test_map_3.png"),
          width: 860,
          height: 310,
          trash_bins: [
            {
              name: "name1",
              color: "#AA00AA",
              x: 200,
              y: 200,
              size: 20,
            },
            {
              name: "name2",
              color: "#AAAA00",
              x: 222,
              y: 200,
              size: 20,
            },
            {
              name: "name3",
              color: "#00AAAA",
              x: 244,
              y: 200,
              size: 20,
            },
          ],
        },
      ],
    };
  },
  methods: {
    change_floor(floor) {
      this.current_floor = floor.id;
    },
  },
};
</script>

<style scoped>
.trash-map-container {
  display: flex;
}
</style>
