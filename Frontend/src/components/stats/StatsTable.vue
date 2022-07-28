<template>
  <div>
    <vue-good-table
      :columns="columns"
      :rows="rows"
      :search-options="{ enabled: true, placeholder: '검색어를 입력하세요.' }"
      :pagination-options="{ enabled: true, mode: 'records' }"
      theme="polar-bear"
      styleClass="vgt-table
    condensed"
      max-height="500px"
      :fixed-header="true"
      compactMode
    >
      <template #emptystate>This will show up when there are no rows</template>
    </vue-good-table>
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
          label: "Index",
          field: "id",
          type: "number",
        },
        {
          label: "쓰레기통 ID",
          field: "trashcanId",
          type: "number",
        },
        {
          label: "최종 수거 시간",
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
          label: "쓰레기 종류",
          field: "trashType",
        },
      ],
      rows: [
        {
          id: 1,
          trashcanId: 11010201,
          latestCollectionTime: "2022-07-27 15:30:11",
          location: "A동2층1구역",
          trashType: "Glass",
        },
        {
          id: 2,
          trashcanId: 11030103,
          latestCollectionTime: "2022-07-26 11:32:41",
          location: "C동1층3구역",
          trashType: "Can",
        },
        {
          id: 3,
          trashcanId: 11020402,
          latestCollectionTime: "2022-07-25 09:34:44",
          location: "B동4층2구역",
          trashType: "Paper",
        },
        {
          id: 4,
          trashcanId: 11010101,
          latestCollectionTime: "2022-07-26 20:10:44",
          location: "A동1층1구역",
          trashType: "Plastic",
        },
        {
          id: 5,
          trashcanId: 11010201,
          latestCollectionTime: "2022-07-26 11:32:41",
          location: "A동2층1구역",
          trashType: "Garbage",
        },
      ],
    };
  },
};
</script>
