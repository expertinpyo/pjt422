<template>
  <div
    class="modal fade"
    id="settings-building-modal"
    tabindex="-1"
    aria-labelledby="settings-building-modal-label"
    aria-hidden="true"
    ref="modal"
  >
    <div class="modal-dialog modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="settings-building-modal-label">
            {{ modalData.title }}
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">...</div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
  <div class="settings-building-container">
    <div class="select-container">
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
          <i class="bi bi-pencil select-icons" @click="modifyBuilding"></i>
          <i class="bi bi-plus-circle select-icons" @click="addBuilding"></i>
        </div>
      </div>
      <div>
        층
        <div class="select-div">
          <select class="form-select" v-model="currentFloor">
            <option v-for="floor in floors" :key="floor.id" :value="floor.id">
              {{ floor.name }}
            </option>
          </select>
          <i class="bi bi-pencil select-icons" @click="modifyFloor"></i>
          <i class="bi bi-plus-circle select-icons" @click="addFloor"></i>
        </div>
      </div>
    </div>
    <hr />
    <div class="trashmap-container" v-if="Object.keys(floors).length">
      <div>
        쓰레기통 (x,y)
        <ul class="list-group trashbin-list">
          <li
            class="list-group-item"
            v-for="(trashbin, idx) in floors[currentFloor].trashbins"
            :key="trashbin.id"
          >
            <b>{{ trashbin.name }}</b>
            <br />
            ({{ trashbin.x }}, {{ trashbin.y }})
            <i
              class="bi bi-pencil select-icons trashbin-list-edit-icon"
              @click="modifyTrashbin(idx)"
            ></i>
          </li>
          <li class="list-group-item">
            <i class="bi bi-plus-circle select-icons" @click="addTrashbin"></i>
          </li>
        </ul>
      </div>
      <TrashMap
        :floor="floors[currentFloor]"
        :width="mapWidth"
        :height="mapHeight"
      />
    </div>
  </div>
</template>

<script>
import TrashMap from "@/components/trashmap/TrashMap.vue";
import { Modal } from "bootstrap";
export default {
  name: "SettingsBuilding",
  components: { TrashMap },
  data() {
    return {
      currentBuilding: 0,
      currentFloor: 0,
      buildings: {},
      floors: {},
      trashbins: [],
      mapWidth: 600,
      mapHeight: 600,
      modalData: {
        title: "Title",
        data: [],
      },
    };
  },
  watch: {
    async currentBuilding(buildingId) {
      if (buildingId === 0) return;
      try {
        await this.fetchFloors();
      } catch (err) {
        // console.log(err);
      }
    },
    async currentFloor(floorId) {
      if (floorId === 0) return;
      try {
        await this.fetchTrashbins();
      } catch (err) {
        // console.log(err);
      }
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

      this.currentBuilding = 0;
      if (Object.keys(this.buildings).length) {
        this.currentBuilding =
          this.buildings[Object.keys(this.buildings)[0]].id;
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
        };
        return prev;
      }, {});

      this.currentFloor = 0;
      if (Object.keys(this.floors).length) {
        this.currentFloor = this.floors[Object.keys(this.floors)[0]].id;
      }
    },
    async fetchTrashbins() {
      const resTrashbins = await this.$axios.get(
        "/api/v1/floor/" + this.currentFloor
      );

      this.trashbins = resTrashbins.data.trashbin.map((el) => {
        return {
          id: el.id,
          name: el.token,
          x: el.location_x,
          y: el.location_y,
          color: "#00AA00",
          hasNotification: false,
        };
      });
      this.floors[this.currentFloor].trashbins = this.trashbins;
    },
    modifyBuilding() {
      const building = this.buildings[this.currentBuilding];
      console.log("modifyBuilding", building);
      this.modalData = {
        title: "건물 편집",
        data: [],
      };
      this.modal.show();
    },
    addBuilding() {
      console.log("addBuilding");
      this.modalData = {
        title: "건물 추가",
        data: [],
      };
      this.modal.show();
    },
    modifyFloor() {
      const floor = this.floors[this.currentFloor];
      console.log("modifyFloor", floor);
      this.modalData = {
        title: "층 편집",
        data: [],
      };
      this.modal.show();
    },
    addFloor() {
      console.log("addFloor");
      this.modalData = {
        title: "층 추가",
        data: [],
      };
      this.modal.show();
    },
    modifyTrashbin(trashbinIdx) {
      const trashbin = this.trashbins[trashbinIdx];
      console.log("modifyTrashbin", trashbin);
      this.modalData = {
        title: "쓰레기통 편집",
        data: [],
      };
      this.modal.show();
    },
    addTrashbin() {
      console.log("addTrashbin");
      this.modalData = {
        title: "쓰레기통 추가",
        data: [],
      };
      this.modal.show();
    },
  },
  async created() {
    try {
      await this.fetchBuildings();
    } catch (err) {
      // err
    }
  },
  mounted() {
    this.modal = new Modal(this.$refs.modal);
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
