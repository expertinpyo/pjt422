<template>
  <div>
    <div class="trash-map-building-dropdown">
      <label for="building-select"><b>건물명</b></label>
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
      <input type="text" placeholder="날짜를 입력해주세요" v-model="date" />
    </div>
    <div class="d-flex justify-content-evenly">
      <button
        type="button"
        class="btn btn-light"
        data-bs-toggle="tooltip"
        data-bs-placement="top"
        title="Tooltip on top"
        @click="datas(0)"
      >
        <strong>일간 데이터</strong>
      </button>
      <button
        type="button"
        class="btn btn-light"
        data-bs-toggle="tooltip"
        data-bs-placement="right"
        title="Tooltip on right"
        @click="datas(1)"
      >
        <strong>주간 데이터</strong>
      </button>
      <button
        type="button"
        class="btn btn-light"
        data-bs-toggle="tooltip"
        data-bs-placement="bottom"
        title="Tooltip on bottom"
        @click="datas(2)"
      >
        <strong>월간 데이터</strong>
      </button>
      <button
        type="button"
        class="btn btn-light"
        data-bs-toggle="tooltip"
        data-bs-placement="left"
        title="Tooltip on left"
        @click="datas(3)"
      >
        <strong>연간 데이터</strong>
      </button>
    </div>
    <div class="trash-stats-chart d-flex justify-content-evenly">
      <StatsBarChart :statsData="statsData.data" />
      <StatsCircleChart :statsData="statsData.data" />
    </div>
  </div>
</template>

<script>
import StatsBarChart from "@/components/stats/StatsBarChart.vue";
import StatsCircleChart from "@/components/stats/StatsCircleChart.vue";

export default {
  name: "StatsView",
  components: {
    StatsBarChart,
    StatsCircleChart,
  },
  watch: {
    async currentBuilding(buildingId) {
      if (buildingId === 0) return;
      this.mapToggleChecked = false;
      try {
        await this.fetchFloors();
      } catch (err) {
        // console.log(err);
      }
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
      date: "",
      dataMethod: 0,
      statsData: {},
    };
  },
  methods: {
    async fetchBuildings() {
      const resBuildings = await this.$axios.get("/api/v1/building");
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
    async fetchStats(number) {
      let link = "/api/v1/stats/building/";

      if (this.date != "") {
        if (number == 0) {
          link += String(this.currentBuilding) + "/" + this.date + "/";
        } else if (number == 1) {
          link += String(this.currentBuilding) + "/week/" + this.date + "/";
        } else if (number == 2) {
          link +=
            String(this.currentBuilding) +
            "/month/" +
            this.date.substr(0, 6) +
            "/";
        } else if (number == 3) {
          link +=
            String(this.currentBuilding) +
            "/year/" +
            this.date.substr(0, 4) +
            "/";
        }
        const ret = await this.$axios.get(link);
        this.statsData = ret;
      }
    },
    datas(number) {
      return this.fetchStats(number);
    },
  },
  async created() {
    try {
      await this.fetchBuildings();
    } catch (err) {
      // console.log(err);
    }
  },
};
</script>

<style>
#app {
  font-family: NanumBarunGothic;
}
.trash-empty-list {
  margin: 80px 15px;
}
.trash-stats-chart {
  margin: 80px 15px;
}
.stats-label {
  margin-bottom: 10px;
  text-align: left;
  font-size: large;
  font-weight: bold;
}
.nav-link {
  max-width: 120px;
  margin: 5px 10px;
}
</style>
