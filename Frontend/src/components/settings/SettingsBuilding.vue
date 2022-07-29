<template>
  <div class="settings-building-container">
    <div class="select-container">
      <div>
        캠퍼스
        <div class="select-div">
          <select class="form-select" v-model="currentCampus">
            <option
              v-for="campus in campuses"
              :key="campus.id"
              :value="campus.id"
            >
              {{ campus.name }}
            </option>
          </select>
          <i class="bi bi-pencil select-icons"></i>
          <i class="bi bi-plus-circle select-icons"></i>
        </div>
      </div>
      <div>
        건물
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
          <i class="bi bi-pencil select-icons"></i>
          <i class="bi bi-plus-circle select-icons"></i>
        </div>
      </div>
      <div>
        층
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
          <i class="bi bi-pencil select-icons"></i>
          <i class="bi bi-plus-circle select-icons"></i>
        </div>
      </div>
    </div>
    <hr />
    <div class="trashmap-container">
      <div>
        쓰레기통 (x,y)
        <ul class="list-group trashbin-list">
          <li
            class="list-group-item"
            v-for="trashbin in floor.trashbins"
            :key="trashbin.id"
          >
            <b>{{ trashbin.name }}</b>
            ({{ trashbin.x }}, {{ trashbin.y }})
            <i class="bi bi-pencil select-icons trashbin-list-edit-icon"></i>
          </li>
          <li class="list-group-item">
            <i class="bi bi-plus-circle select-icons"></i>
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
      currentCampus: 0,
      currentBuilding: 0,
      currentFloor: 0,
      campuses: {},
      buildings: {},
      floors: {},
      floor: {},
      mapWidth: 600,
      mapHeight: 600,
    };
  },
  watch: {
    currentCampus() {
      this.fetchBuildings();
    },
    currentBuilding() {
      this.fetchFloors();
    },
    currentFloor() {
      this.fetchCurrentFloor();
    },
  },
  methods: {
    async fetchCampuses() {
      const resCampuses = await this.$axios.get("/api/v1/campus");
      this.campuses = resCampuses.data.reduce((prev, cur) => {
        prev[cur.pk] = {
          id: cur.pk,
          name: cur.name,
        };
        return prev;
      }, {});

      if (Object.keys(this.campuses).length) {
        this.currentCampus = this.campuses[Object.keys(this.campuses)[0]].id;
        await this.fetchBuildings();
      }
    },
    async fetchBuildings() {
      const resBuildings = await this.$axios.get(
        "/api/v1/campus/" + this.currentCampus
      );
      this.buildings = resBuildings.data.building.reduce((prev, cur) => {
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
        "/api/v1/campus/building/" + this.currentBuilding
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
        SAF: "#00AA00",
        CAU: "#AAAA00",
        WAR: "#AA0000",
      };

      const resTrashbins = await this.$axios.get(
        "/api/v1/campus/floor/" + this.currentFloor
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
      this.fetchCampuses();
    } catch (err) {
      // err
    }
  },
};
</script>

<style scoped>
.select-container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  margin: 10px;
}
.select-div {
  display: flex;
}
.select-icons {
  font-size: larger;
  align-self: center;
  margin: 0 5px;
}
.trashmap-container {
  display: flex;
  margin: 10px;
}
.trashbin-list {
  min-width: 250px;
  margin-right: 10px;
  padding-right: 40px;
  overflow-y: scroll;
}
.list-group-item {
  position: relative;
}
.trashbin-list-edit-icon {
  position: absolute;
  right: -32px;
}
</style>
