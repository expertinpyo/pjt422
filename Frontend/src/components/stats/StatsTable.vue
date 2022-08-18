<template>
  <div>
    <vue-good-table :columns="columns" :rows="rows" />
  </div>
</template>

<script>
import "vue-good-table-next/dist/vue-good-table-next.css";
import { VueGoodTable } from "vue-good-table-next";

export default {
  name: "StatsTable",
  components: {
    VueGoodTable,
  },
  data() {
    return {
      columns: [
        {
          label: "번호",
          field: "id",
          type: "number",
        },
        {
          label: "쓰레기통 ID",
          field: "trashcanId",
          type: "number",
        },
        {
          label: "날짜 및 시각",
          field: "latestCollectionTime",
          type: "date",
          dateInputFormat: "yyyy-MM-dd HH:mm:ss",
          dateOutputFormat: "yyyy-MM-dd HH:mm:ss",
        },
        {
          label: "위치",
          field: "location",
        },
        {
          label: "쓰레기통 분류",
          field: "trashType",
        },
      ],
      rows: [
        {
          id: 1,
          trashcanId: 11010201,
          latestCollectionTime: "2022-07-27 15:30:11",
          location: "공학관 2층 1구역",
          trashType: "유리",
        },
        {
          id: 2,
          trashcanId: 11030103,
          latestCollectionTime: "2022-07-26 11:32:41",
          location: "어학관 1층 3구역",
          trashType: "캔",
        },
        {
          id: 3,
          trashcanId: 11020402,
          latestCollectionTime: "2022-07-25 09:34:44",
          location: "중앙도서관 4층 2구역",
          trashType: "종이",
        },
        {
          id: 4,
          trashcanId: 11010101,
          latestCollectionTime: "2022-07-26 20:10:44",
          location: "공학관 1층 1구역",
          trashType: "플라스틱",
        },
        {
          id: 5,
          trashcanId: 11010201,
          latestCollectionTime: "2022-07-26 11:32:41",
          location: "경영대학관 2층 1구역",
          trashType: "일반",
        },
      ],
    };
  },
};
</script>
