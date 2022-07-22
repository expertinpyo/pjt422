<template>
  <div class="main-container">
    <div class="trash-map-selector-container">
      <div class="trash-map-campus-dropdown">
        <label for="campus-select">캠퍼스</label>
        <select id="campus-select" class="form-select" v-model="currentCampus">
          <option
            v-for="campus in campuses"
            :key="campus.id"
            :value="campus.id"
          >
            {{ campus.name }}
          </option>
        </select>
      </div>
      <div class="trash-map-building-dropdown">
        <label for="building-select">건물</label>
        <select
          id="building-select"
          class="form-select"
          v-model="currentBuilding"
        >
          <option
            v-for="building in buildings"
            :key="building.id"
            :value="building.id"
          >
            {{ building.name }}
          </option>
        </select>
      </div>
      <TrashMapFloorSelector
        :floors="floors"
        :current-floor="currentFloor"
        @floor-changed="changeFloor"
      />
    </div>
    <div class="trash-map-container">
      <div class="form-check form-switch trash-map-toggle">
        <input
          class="form-check-input"
          type="checkbox"
          id="map-toggle"
          v-model="mapToggleChecked"
        />
        <label class="form-check-label" for="map-toggle">전체 층 보기</label>
      </div>
      <div v-if="mapToggleChecked" class="trash-map-group">
        <div v-for="floor in floors" :key="floor.id" class="trash-map">
          <div>
            <label :for="'trash-map-' + floor.id">{{ floor.name }}F</label>
          </div>
          <TrashMap
            :id="'trash-map-' + floor.id"
            :floor="floor"
            :width="mapWidth"
            :height="mapHeight"
          />
        </div>
      </div>
      <div v-if="!mapToggleChecked" class="trash-map-group">
        <div class="trash-map">
          <TrashMap
            :floor="floors[currentFloor]"
            :width="mapWidth"
            :height="mapHeight"
          />
        </div>
      </div>
    </div>
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
  watch: {
    mapToggleChecked() {
      this.currentFloor = -(1 + this.currentFloor);
    },
    currentFloor() {
      if (this.mapToggleChecked && this.currentFloor >= 0) {
        this.mapToggleChecked = false;
        this.currentFloor = -(1 + this.currentFloor);
      }
    },
    "$store.state.hoveredTrashbin"() {
      // hover event
    },
    "$store.state.selectedTrashbin"() {
      // select event
    },
  },
  computed: {
    mapWidth() {
      const width = this.windowWidth - 150;
      const columns = this.mapToggleChecked
        ? Math.max(1, Math.floor(width / 312))
        : 1;
      const columnWidth = width / columns - 12;

      return Math.max(300, columnWidth);
    },
    mapHeight() {
      return Math.min(this.mapWidth, window.innerHeight - 120);
    },
  },
  data() {
    return {
      windowWidth: window.innerWidth,
      mapToggleChecked: false,
      currentCampus: 0,
      currentBuilding: 0,
      currentFloor: 0,
      campuses: [
        { id: 0, name: "서울" },
        { id: 1, name: "부산" },
      ],
      buildings: [
        { id: 0, name: "공학관" },
        { id: 1, name: "도서관" },
      ],
      floors: [
        {
          id: 0,
          name: "B1",
          src: require("@/assets/test_map_b1.png"),
          width: 860,
          height: 310,
          trashbins: [
            {
              id: 0,
              name: "name1",
              color: "#AA0000",
              x: 200,
              y: 200,
              size: 20,
            },
            {
              id: 1,
              name: "name2",
              color: "#00AA00",
              x: 222,
              y: 200,
              size: 20,
            },
            {
              id: 2,
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
          trashbins: [
            {
              id: 3,
              name: "name1",
              color: "#AAAA00",
              x: 200,
              y: 200,
              size: 20,
            },
            {
              id: 4,
              name: "name2",
              color: "#00AAAA",
              x: 222,
              y: 200,
              size: 20,
            },
            {
              id: 5,
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
          trashbins: [
            {
              id: 6,
              name: "name1",
              color: "#0000AA",
              x: 200,
              y: 200,
              size: 20,
            },
            {
              id: 7,
              name: "name2",
              color: "#AA0000",
              x: 222,
              y: 200,
              size: 20,
            },
            {
              id: 8,
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
          trashbins: [
            {
              id: 9,
              name: "name1",
              color: "#AA00AA",
              x: 200,
              y: 200,
              size: 20,
            },
            {
              id: 10,
              name: "name2",
              color: "#AAAA00",
              x: 222,
              y: 200,
              size: 20,
            },
            {
              id: 11,
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
    changeFloor(floor) {
      this.currentFloor = floor.id;
    },
  },
  mounted() {
    window.addEventListener("resize", () => {
      this.windowWidth = window.innerWidth;
    });
  },
};
</script>

<style scoped>
.main-container {
  display: flex;
  margin-top: 10px;
}
.trash-map-selector-container {
  width: 131px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5px;
  border-right: 1px solid black;
}
.trash-map-campus-dropdown {
  width: 120px;
  margin-bottom: 10px;
}
.trash-map-building-dropdown {
  width: 120px;
  margin-bottom: 30px;
}
.trash-map-container {
  width: 100%;
}
.trash-map-toggle {
  width: 140px;
  margin-left: auto;
  margin-right: 0;
}
.trash-map-group {
  display: flex;
  flex-wrap: wrap;
}
.trash-map {
  margin: 5px;
}
</style>
