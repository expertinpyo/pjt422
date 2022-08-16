<template>
  <div class="stats-container">
    <div class="trash-empty-list">
      <div class="stats-label">쓰레기통 비움 목록</div>
      <StatsTable />
    </div>
    <div class="trash-stats-chart">
      <div class="stats-label">월별 쓰레기 배출량</div>
      <StatsChart />
    </div>
  </div>
</template>

<script>
import StatsTable from "@/components/stats/StatsTable.vue";
import StatsChart from "@/components/stats/StatsChart.vue";

export default {
  name: "StatsView",
  components: {
    StatsTable,
    StatsChart,
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
</style>
