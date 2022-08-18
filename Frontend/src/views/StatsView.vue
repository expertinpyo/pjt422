<template>
  <h1>StatsView</h1>
  <h3>TableHere</h3>
  <StatsTable />
  <h3>ChartHere</h3>
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
