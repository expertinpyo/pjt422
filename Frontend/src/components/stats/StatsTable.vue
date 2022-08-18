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
          label: "Index",
          field: "id",
          type: "number",
        },
        {
          label: "TrashcanID",
          field: "trashcanId",
          type: "number",
        },
        {
          label: "Latest collection time",
          field: "latestCollectionTime",
          type: "date",
          dateInputFormat: "yyyy-MM-dd HH:mm:ss",
          dateOutputFormat: "yyyy-MM-dd HH:mm:ss",
        },
        {
          label: "Location",
          field: "location",
        },
        {
          label: "Trash Type",
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
