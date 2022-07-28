<template>
  <h1>StatsView</h1>
  <p>쓰레기통 비움 목록</p>
  <StatsTable />
  <p>재활용 쓰레기 종류별 배출량</p>
  <StatsChart />
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
