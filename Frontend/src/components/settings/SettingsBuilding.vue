<template>
  <div class="settings-building-container">
    <div class="select-container">
      <div class="building-select">
        <div class="select-div">
          <select class="form-select" v-model="currentBuilding">
            <option
              v-for="building in buildings"
              :key="building.id"
              :value="building.id"
            >
              {{ building.name }}
            </option>
          </select>
          <img src="@/assets/edit.png" class="select-icons" />
          <img src="@/assets/add.png" class="select-icons" />
        </div>
      </div>
      <div class="floor-select">
        <div class="select-div">
          <select class="form-select" v-model="currentFloor">
            <option
              v-for="floor_ in floors"
              :key="floor_.id"
              :value="floor_.id"
            >
              {{ floor_.name }}
            </option>
          </select>
          <img src="@/assets/edit.png" class="select-icons" />
          <img src="@/assets/add.png" class="select-icons" />
        </div>
      </div>
    </div>
    <hr />
    <div class="trashmap-container">
      <div class="trashmap-select">
        <label>쓰레기통 목록 (x, y)</label>
        <ul class="list-group trashbin-list">
          <li
            class="list-group-item"
            v-for="trashbin in floor.trashbins"
            :key="trashbin.id"
          >
            <b>{{ trashbin.name }}</b>
            ({{ trashbin.x }}, {{ trashbin.y }})
            <img
              src="@/assets/edit.png"
              class="select-icons trashbin-list-edit-icon"
            />
          </li>
          <li class="list-group-item">
            <img src="@/assets/add.png" class="select-icons" />
          </li>
        </ul>
      </div>
      <TrashMap
        v-if="Object.keys(floor).length"
        :floor="floor"
        :width="mapWidth"
        :height="mapHeight"
      />
    </div>
  </div>
</template>

<script>
import TrashMap from "@/components/trashmap/TrashMap.vue";
export default {
  name: "SettingsBuilding",
  components: { TrashMap },
  data() {
    return {
      currentBuilding: 0,
      currentFloor: 0,
      buildings: {},
      floors: {},
      floor: {},
      mapWidth: 600,
      mapHeight: 600,
    };
  },
  watch: {
    currentBuilding() {
      this.fetchFloors();
    },
    currentFloor() {
      this.fetchCurrentFloor();
    },
  },
  methods: {
    async fetchBuildings() {
      const resBuildings = await this.$axios.get("/api/v1/building/");
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
        };
        return prev;
      }, {});

      if (Object.keys(this.floors).length) {
        this.currentFloor = this.floors[Object.keys(this.floors)[0]].id;
        await this.fetchCurrentFloor();
      }
    },
    async fetchCurrentFloor() {
      const trashbin_colormap = {
        SAF: "#CEDDC9",
        CAU: "#F2DCB1",
        WAR: "#DE9F9F",
      };

      const resTrashbins = await this.$axios.get(
        "/api/v1/floor/" + this.currentFloor
      );
      const floor = resTrashbins.data;
      const trashbins = floor.trashbin.map((el) => {
        return {
          id: el.id,
          name: el.token,
          x: el.location_x,
          y: el.location_y,
          color: trashbin_colormap[el.status],
        };
      });
      this.floor = {
        id: floor.pk,
        name: floor.name,
        width: floor.width,
        height: floor.height,
        src: floor.map_path,
        trashbinSize: floor.trashbin_size,
        trashbins: trashbins,
      };
    },
  },
  created() {
    try {
      this.fetchBuildings();
    } catch (err) {
      // err
    }
  },
};
</script>

<style scoped>
#SettingBuilding {
  font-family: "Pretendard-Regular";
}
.select-container {
  display: flex;
  justify-content: flex-end;
  margin: 10px 0;
}
.select-div {
  display: flex;
  margin-right: 25px;
}
.select-icons {
  align-self: center;
  margin: 0 4px;
  width: 20px;
  height: 20px;
}
.trashmap-container {
  display: flex;
  margin-top: 50px;
}
.trashmap-select {
  margin-left: 40px;
  margin-right: 100px;
}
.trashbin-list {
  min-width: 300px;
  margin-right: 10px;
  padding-right: 40px;
  overflow-y: scroll;
}
.list-group-item {
  position: relative;
  height: 40px;
}
.trashbin-list-edit-icon {
  position: absolute;
  right: -32px;
}
</style>
