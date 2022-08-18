<template>
  <div>
    <strong>쓰레기통 시간대별 사용량</strong>
    <Line
      :chart-options="chartOptions"
      :chart-data="chartData"
      :width="width"
      :height="height"
    />
  </div>
</template>

<script>
import { Line } from "vue-chartjs";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

export default {
  name: "Line-Line",
  components: { Line },
  props: {
    width: {
      type: Number,
      default: 800,
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
        labels: [
          "00시",
          "01시",
          "02시",
          "03시",
          "04시",
          "05시",
          "06시",
          "07시",
          "08시",
          "09시",
          "10시",
          "11시",
          "12시",
          "13시",
          "14시",
          "15시",
          "16시",
          "17시",
          "18시",
          "19시",
          "20시",
          "21시",
          "22시",
          "23시",
        ],
        datasets: [
          {
            label: "usage",
            data: [
              dataStat.hour_00,
              dataStat.hour_01,
              dataStat.hour_02,
              dataStat.hour_03,
              dataStat.hour_04,
              dataStat.hour_05,
              dataStat.hour_06,
              dataStat.hour_07,
              dataStat.hour_08,
              dataStat.hour_09,
              dataStat.hour_10,
              dataStat.hour_11,
              dataStat.hour_12,
              dataStat.hour_13,
              dataStat.hour_14,
              dataStat.hour_15,
              dataStat.hour_16,
              dataStat.hour_17,
              dataStat.hour_18,
              dataStat.hour_19,
              dataStat.hour_20,
              dataStat.hour_21,
              dataStat.hour_22,
              dataStat.hour_23,
            ],
            borderColor: "rgb(0, 204, 0)",
          },
        ],
      };
    },
  },
  data() {
    return {
      chartData: {
        labels: [
          "00시",
          "01시",
          "02시",
          "03시",
          "04시",
          "05시",
          "06시",
          "07시",
          "08시",
          "09시",
          "10시",
          "11시",
          "12시",
          "13시",
          "14시",
          "15시",
          "16시",
          "17시",
          "18시",
          "19시",
          "20시",
          "21시",
          "22시",
          "23시",
        ],
        datasets: [
          { label: "usage", data: [], backgroundColor: ["rgb(192, 192, 192)"] },
        ],
      },
      chartOptions: {
        responsive: true,
      },
      total: 0,
    };
  },
};
</script>
<style></style>
