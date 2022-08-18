<template>
  <div>
    <strong>쓰레기통 종류별 사용량</strong>
    <Doughnut
      :chart-data="chartData"
      :options="chartOptions"
      :width="width"
      :height="height"
    />
  </div>
</template>

<script>
import { Doughnut } from "vue-chartjs";
import { Chart as ChartJS, ArcElement } from "chart.js";

ChartJS.register(ArcElement);

export default {
  name: "CircleChart",
  components: { Doughnut },
  props: {
    width: {
      type: Number,
      default: 400,
    },
    height: {
      type: Number,
    },
    statsData: {
      type: Object,
    },
  },
  watch: {
    statsData(dataStat) {
      this.total = dataStat.total;
      this.chartData = {
        labels: ["일반", "플라스틱", "캔", "종이", "유리"],
        datasets: [
          {
            data: [
              dataStat.GER,
              dataStat.PET,
              dataStat.CAN,
              dataStat.PPR,
              dataStat.GLA,
            ],
            backgroundColor: [
              "rgb(255, 102, 102)",
              "rgb(255, 255, 102)",
              "rgb(192, 192, 192)",
              "rgb(102, 255, 102)",
              "rgb(102, 178, 255)",
            ],
          },
        ],
      };
    },
  },
  data() {
    return {
      chartData: {
        labels: ["일반", "플라스틱", "캔", "종이", "유리"],
        datasets: [
          {
            data: [0, 0, 0, 0, 0],
            backgroundColor: [
              "rgb(255, 102, 102)",
              "rgb(255, 255, 102)",
              "rgb(192, 192, 192)",
              "rgb(102, 255, 102)",
              "rgb(102, 178, 255)",
            ],
          },
        ],
      },
      chartOptions: {
        responsive: true,
      },
    };
  },
};
</script>
<style></style>
