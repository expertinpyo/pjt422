<template>
  <div class="main-container">
    <div class="trash-map-selector-container">
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
    <div class="trash-map-container" v-if="Object.keys(floors).length">
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
import TrashMap from "@/components/trashmap/TrashMap.vue";

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
    async currentBuilding() {
      this.mapToggleChecked = false;
      try {
        await this.fetchFloors();
      } catch (err) {
        // console.log(err);
      }
    },
    async currentFloor() {
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
      const width = this.windowWidth - 180;
      const columns = this.mapToggleChecked
        ? Math.max(1, Math.floor(width / 312))
        : 1;
      const columnWidth = width / columns - 12;

      return Math.max(300, columnWidth);
    },
    mapHeight() {
      return Math.min(this.mapWidth, window.innerHeight - 120);
    },
    notifications() {
      return this.$store.state.notifications;
    },
  },
  data() {
    return {
      windowWidth: window.innerWidth,
      mapToggleChecked: false,
      currentBuilding: 0,
      currentFloor: 0,
      buildings: {},
      floors: {},
    };
  },
  methods: {
    changeFloor(floor) {
      this.currentFloor = floor.id;
    },
    async fetchBuildings() {
      const resBuildings = await this.$axios.get("/api/v1/building");
      console.log(resBuildings.data);
      this.buildings = resBuildings.data.reduce((prev, cur) => {
        prev[cur.pk] = {
          id: cur.pk,
          name: cur.name,
        };
        return prev;
      }, {});

      if (Object.keys(this.buildings).length) {
        this.currentBuilding =
          this.buildings[Object.keys(this.buildings)[0]].id;
        await this.fetchFloors();
      }
    },
    async fetchFloors() {
      const resFloors = await this.$axios.get(
        "/api/v1/building/" + this.currentBuilding
      );
      this.floors = resFloors.data.floor.reduce((prev, cur) => {
        prev[cur.pk] = {
          id: cur.pk,
          name: cur.name,
          width: cur.width,
          height: cur.height,
          src: cur.map_path,
          trashbinSize: cur.trashbin_size,
          trashbins: [],
          notificationCount: 0,
        };
        return prev;
      }, {});

      const trashbin_colormap = {
        SAF: "#00AA00",
        CAU: "#AAAA00",
        WAR: "#AA0000",
      };

      const notificationIds = this.notifications.map((el) => el.id);

      Object.keys(this.floors).forEach(async (floor_id) => {
        const resTrashbins = await this.$axios.get("/api/v1/floor/" + floor_id);

        let notificationCount = 0;
        this.floors[floor_id].trashbins = resTrashbins.data.trashbin.map(
          (el) => {
            let hasNotification = false;
            if (notificationIds.includes(el.id)) {
              hasNotification = true;
              notificationCount++;
            }
            return {
              id: el.id,
              name: el.trash_type,
              x: el.location_x,
              y: el.location_y,
              color: trashbin_colormap[el.status],
              hasNotification,
            };
          }
        );

        this.floors[floor_id].notificationCount = notificationCount;
      });

      if (Object.keys(this.floors).length) {
        this.currentFloor = this.floors[Object.keys(this.floors)[0]].id;
      }
    },
  },
  async created() {
    window.addEventListener("resize", () => {
      this.windowWidth = window.innerWidth;
    });

    try {
      await this.$store.dispatch("getNotifications");
      await this.fetchBuildings();
    } catch (err) {
      // console.log(err);
    }
  },
};
</script>

<style scoped>
.main-container {
  display: flex;
  margin-top: 10px;
}
.trash-map-selector-container {
  width: 161px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5px;
  border-right: 1px solid black;
}
.trash-map-campus-dropdown {
  width: 150px;
  margin-bottom: 10px;
}
.trash-map-building-dropdown {
  width: 150px;
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
