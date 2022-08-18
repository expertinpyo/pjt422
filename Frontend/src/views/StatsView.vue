<template>
  <div class="stats-container">
    <div class="trash-empty-list">
      <div class="stats-label">쓰레기통 비움 목록</div>
      <StatsTable />
    </div>
    <div class="trash-stats-chart">
      <div class="stats-label">쓰레기통 사용량 통계</div>
      <StatsPage />
    </div>
  </div>
</template>

<script>
import StatsTable from "@/components/stats/StatsTable.vue";
import StatsPage from "@/components/stats/StatsPage.vue";

export default {
  name: "StatsView",
  components: {
    StatsTable,
    StatsPage,
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
.trash-map-building-dropdown {
  width: 150px;
  margin-bottom: 30px;
}
.nav-link {
  max-width: 120px;
  margin: 5px 10px;
}
.nav-link.active {
  /* border-bottom: 1px solid black; */
}
.navbar-brandname {
  font-size: 18px;
  font-weight: bolder;
  padding: 0 10px;
}
.nav-item-logout {
  padding: 5px;
  border-radius: 10px;
  /* background-color: #a5b8a5; */
}
</style>
