<template>
  <div class="main-container">
    <div class="trash-map-selector-container">
      <div class="trash-map-campus-dropdown">
        <label for="campus_select">캠퍼스</label>
        <select id="campus_select" class="form-select" v-model="current_campus">
          <option
            v-for="campus in campuses"
            :key="campus.id"
            :value="campus.id"
          >
            {{ campus.name }}
          </option>
        </select>
      </div>
      <div class="trash-map-building-dropdown">
        <label for="building_select">건물</label>
        <select
          id="building_select"
          class="form-select"
          v-model="current_building"
        >
          <option
            v-for="building in buildings"
            :key="building.id"
            :value="building.id"
          >
            {{ building.name }}
          </option>
        </select>
      </div>
      <TrashMapFloorSelector
        :floors="floors"
        :current_floor="current_floor"
        @floor_changed="change_floor"
      />
    </div>
    <div class="trash-map-container">
      <div class="form-check form-switch trash-map-toggle">
        <input
          class="form-check-input"
          type="checkbox"
          id="map_toggle"
          v-model="map_toggle_checked"
        />
        <label class="form-check-label" for="map_toggle">전체 층 보기</label>
      </div>
      <div v-if="map_toggle_checked" class="trash-map-group">
        <div v-for="floor in floors" :key="floor.id" class="trash-map">
          <div>
            <label :for="'trash_map_' + floor.id">{{ floor.name }}F</label>
          </div>
          <TrashMap
            :id="'trash_map_' + floor.id"
            :floor="floor"
            :width="map_width"
            :height="map_height"
            @trash_bin_event="trash_bin_event"
          />
        </div>
      </div>
      <div v-if="!map_toggle_checked" class="trash-map-group">
        <div class="trash-map">
          <TrashMap
            :floor="floors[current_floor]"
            :width="map_width"
            :height="map_height"
            @trash_bin_event="trash_bin_event"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TrashMapFloorSelector from "@/components/main/TrashMapFloorSelector.vue";
import TrashMap from "@/components/main/TrashMap.vue";

export default {
  name: "MainView",
  components: {
    TrashMapFloorSelector,
    TrashMap,
  },
  watch: {
    map_toggle_checked() {
      this.current_floor = -(1 + this.current_floor);
    },
    current_floor() {
      if (this.map_toggle_checked && this.current_floor >= 0) {
        this.map_toggle_checked = false;
        this.current_floor = -(1 + this.current_floor);
      }
    },
  },
  computed: {
    map_width() {
      const width = this.window_width - 150;
      const columns = this.map_toggle_checked
        ? Math.max(1, Math.floor(width / 312))
        : 1;
      const column_width = width / columns - 12;

      return Math.max(300, column_width);
    },
    map_height() {
      return Math.min(this.map_width, window.innerHeight - 120);
    },
  },
  data() {
    return {
      window_width: window.innerWidth,
      map_toggle_checked: false,
      selected_trash_bin: { floor_id: -1, trash_bin_id: -1 },
      hovered_trash_bin: { floor_id: -1, trash_bin_id: -1 },
      current_campus: 0,
      current_building: 0,
      current_floor: 0,
      campuses: [
        { id: 0, name: "서울" },
        { id: 1, name: "부산" },
      ],
      buildings: [
        { id: 0, name: "공학관" },
        { id: 1, name: "도서관" },
      ],
      floors: [
        {
          id: 0,
          name: "B1",
          src: require("@/assets/test_map_b1.png"),
          width: 860,
          height: 310,
          trash_bins: [
            {
              id: 0,
              name: "name1",
              color: "#AA0000",
              x: 200,
              y: 200,
              size: 20,
              hovered: false,
              selected: false,
            },
            {
              id: 1,
              name: "name2",
              color: "#00AA00",
              x: 222,
              y: 200,
              size: 20,
              hovered: false,
              selected: false,
            },
            {
              id: 2,
              name: "name3",
              color: "#0000AA",
              x: 244,
              y: 200,
              size: 20,
              hovered: false,
              selected: false,
            },
          ],
        },
        {
          id: 1,
          name: "1",
          src: require("@/assets/test_map_1.png"),
          width: 860,
          height: 310,
          trash_bins: [
            {
              id: 3,
              name: "name1",
              color: "#AAAA00",
              x: 200,
              y: 200,
              size: 20,
              hovered: false,
              selected: false,
            },
            {
              id: 4,
              name: "name2",
              color: "#00AAAA",
              x: 222,
              y: 200,
              size: 20,
              hovered: false,
              selected: false,
            },
            {
              id: 5,
              name: "name3",
              color: "#AA00AA",
              x: 244,
              y: 200,
              size: 20,
              hovered: false,
              selected: false,
            },
          ],
        },
        {
          id: 2,
          name: "2",
          src: require("@/assets/test_map_2.png"),
          width: 860,
          height: 310,
          trash_bins: [
            {
              id: 6,
              name: "name1",
              color: "#0000AA",
              x: 200,
              y: 200,
              size: 20,
              hovered: false,
              selected: false,
            },
            {
              id: 7,
              name: "name2",
              color: "#AA0000",
              x: 222,
              y: 200,
              size: 20,
              hovered: false,
              selected: false,
            },
            {
              id: 8,
              name: "name3",
              color: "#00AA00",
              x: 244,
              y: 200,
              size: 20,
              hovered: false,
              selected: false,
            },
          ],
        },
        {
          id: 3,
          name: "3",
          src: require("@/assets/test_map_3.png"),
          width: 860,
          height: 310,
          trash_bins: [
            {
              id: 9,
              name: "name1",
              color: "#AA00AA",
              x: 200,
              y: 200,
              size: 20,
              hovered: false,
              selected: false,
            },
            {
              id: 10,
              name: "name2",
              color: "#AAAA00",
              x: 222,
              y: 200,
              size: 20,
              hovered: false,
              selected: false,
            },
            {
              id: 11,
              name: "name3",
              color: "#00AAAA",
              x: 244,
              y: 200,
              size: 20,
              hovered: false,
              selected: false,
            },
          ],
        },
      ],
    };
  },
  methods: {
    change_floor(floor) {
      this.current_floor = floor.id;
    },
    trash_bin_event(ev) {
      if (ev.type === "select") {
        this.selected_trash_bin = ev.trash_bin;
        this.selected_trash_bin.selected = true;
      }
      if (ev.type === "unselect") {
        this.selected_trash_bin.selected = false;
        this.selected_trash_bin = {};
      }
      if (ev.type === "mouseover") {
        this.hovered_trash_bin = ev.trash_bin;
        this.hovered_trash_bin.hovered = true;
      }
      if (ev.type === "mouseout") {
        this.hovered_trash_bin.hovered = false;
        this.hovered_trash_bin = {};
      }
    },
  },
  mounted() {
    window.addEventListener("resize", () => {
      this.window_width = window.innerWidth;
    });
  },
};
</script>

<style scoped>
.main-container {
  display: flex;
  margin-top: 10px;
}
.trash-map-selector-container {
  width: 131px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5px;
  border-right: 1px solid black;
}
.trash-map-campus-dropdown {
  width: 120px;
  margin-bottom: 10px;
}
.trash-map-building-dropdown {
  width: 120px;
  margin-bottom: 30px;
}
.trash-map-container {
  width: 100%;
}
.trash-map-toggle {
  width: 140px;
  margin-left: auto;
  margin-right: 0;
}
.trash-map-group {
  display: flex;
  flex-wrap: wrap;
}
.trash-map {
  margin: 5px;
}
</style>
