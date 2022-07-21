<template>
  <canvas
    ref="canvas"
    @mousedown="mousedown"
    @mousemove.prevent="mousemove"
    @wheel.prevent="wheel"
  ></canvas>
</template>

<script>
export default {
  name: "TrashMap",
  props: ["floor", "width", "height"],
  data() {
    return {
      zoom: 1,
      offset_x: 0,
      offset_y: 0,
      mouse_prev_x: 0,
      mouse_prev_y: 0,
      current_mouseover_trash_bin: -1,
      current_trash_bin: -1,
    };
  },
  watch: {
    floor() {
      this.calc_and_apply_base_values();
      this.load_map_and_draw();
    },
    width() {
      this.canvas.width = this.width;
      this.canvas.height = this.height;
      this.calc_and_apply_base_values();
      this.draw();
    },
    highlighted_trash_bins() {
      this.draw();
    },
  },
  methods: {
    draw() {
      this.ctx.resetTransform();
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
      this.ctx.scale(this.zoom, this.zoom);
      this.ctx.translate(this.offset_x, this.offset_y);

      this.ctx.drawImage(this.img, 0, 0);

      for (let trash_bin of this.floor.trash_bins) {
        this.ctx.save();
        this.ctx.fillStyle = trash_bin.color;
        this.ctx.fillRect(
          trash_bin.x - trash_bin.size / 2,
          trash_bin.y - trash_bin.size / 2,
          trash_bin.size,
          trash_bin.size
        );

        this.ctx.lineWidth = 1;
        this.ctx.strokeStyle = "#000000";
        if (trash_bin.hovered) {
          this.ctx.lineWidth = 2;
          this.ctx.strokeStyle = "#88FF88";
        }
        if (trash_bin.selected) {
          this.ctx.lineWidth = 2;
          this.ctx.strokeStyle = "#FF8888";
        }
        this.ctx.strokeRect(
          trash_bin.x - trash_bin.size / 2,
          trash_bin.y - trash_bin.size / 2,
          trash_bin.size,
          trash_bin.size
        );
        this.ctx.restore();
      }
    },
    load_map_and_draw() {
      this.img = new Image();
      this.img.onload = () => {
        this.draw();
      };
      this.img.src = this.floor.src;
    },
    calc_and_apply_base_values() {
      this.base_zoom = Math.min(
        1,
        this.canvas.width / this.floor.width,
        this.canvas.height / this.floor.height
      );
      this.base_offset_x = Math.max(
        0,
        (this.canvas.width / this.base_zoom - this.floor.width) / 2
      );
      this.base_offset_y = Math.max(
        0,
        (this.canvas.height / this.base_zoom - this.floor.height) / 2
      );

      this.zoom = this.base_zoom;
      this.offset_x = this.base_offset_x;
      this.offset_y = this.base_offset_y;
    },
    change_zoom(zoom_ratio) {
      if (this.zoom * zoom_ratio < this.base_zoom * 0.75) {
        this.zoom = this.base_zoom * 0.75;
      } else if (this.zoom * zoom_ratio > this.base_zoom * 4) {
        this.zoom = this.base_zoom * 4;
      } else {
        this.zoom *= zoom_ratio;
      }
    },
    change_offset(offset_x_delta, offset_y_delta) {
      this.offset_x += offset_x_delta;
      this.offset_y += offset_y_delta;
    },
    mousedown(ev) {
      if ((ev.buttons & 1) === 0) return;
      ev.stopPropagation();

      this.mouse_prev_x = ev.offsetX;
      this.mouse_prev_y = ev.offsetY;

      const canvas_x = -this.offset_x + ev.offsetX / this.zoom;
      const canvas_y = -this.offset_y + ev.offsetY / this.zoom;

      for (let trash_bin of this.floor.trash_bins) {
        const left = trash_bin.x - trash_bin.size / 2;
        const right = trash_bin.x + trash_bin.size / 2;
        const top = trash_bin.y - trash_bin.size / 2;
        const bottom = trash_bin.y + trash_bin.size / 2;

        if (
          canvas_x > left &&
          canvas_x < right &&
          canvas_y > top &&
          canvas_y < bottom
        ) {
          if (this.current_trash_bin == trash_bin.id) {
            return;
          }
          if (this.current_trash_bin >= 0) {
            this.$emit("trash_bin_event", { type: "unselect" });
          }
          this.$emit("trash_bin_event", { type: "select", trash_bin });
          this.current_trash_bin = trash_bin.id;
          this.draw();
          return;
        }
      }
      if (this.current_trash_bin >= 0) {
        this.$emit("trash_bin_event", { type: "unselect" });
        this.current_trash_bin = -1;
        this.draw();
      }
    },
    mousemove(ev) {
      if ((ev.buttons & 1) === 1) {
        this.change_offset(
          (ev.offsetX - this.mouse_prev_x) / this.zoom,
          (ev.offsetY - this.mouse_prev_y) / this.zoom
        );
        this.mouse_prev_x = ev.offsetX;
        this.mouse_prev_y = ev.offsetY;
        this.draw();
      }

      const canvas_x = -this.offset_x + ev.offsetX / this.zoom;
      const canvas_y = -this.offset_y + ev.offsetY / this.zoom;

      for (let trash_bin of this.floor.trash_bins) {
        const left = trash_bin.x - trash_bin.size / 2;
        const right = trash_bin.x + trash_bin.size / 2;
        const top = trash_bin.y - trash_bin.size / 2;
        const bottom = trash_bin.y + trash_bin.size / 2;

        if (
          canvas_x > left &&
          canvas_x < right &&
          canvas_y > top &&
          canvas_y < bottom
        ) {
          if (this.current_mouseover_trash_bin == trash_bin.id) {
            return;
          }

          if (this.current_mouseover_trash_bin >= 0) {
            this.$emit("trash_bin_event", { type: "mouseout" });
          }
          this.$emit("trash_bin_event", { type: "mouseover", trash_bin });
          this.current_mouseover_trash_bin = trash_bin.id;
          this.draw();
          return;
        }
      }
      if (this.current_mouseover_trash_bin >= 0) {
        this.$emit("trash_bin_event", { type: "mouseout" });
        this.current_mouseover_trash_bin = -1;
        this.draw();
      }
    },
    wheel(ev) {
      const prev_zoom = this.zoom;
      if (ev.deltaY < 0) this.change_zoom(1.1);
      else if (ev.deltaY > 0) this.change_zoom(1 / 1.1);
      this.change_offset(
        ev.offsetX / this.zoom - ev.offsetX / prev_zoom,
        ev.offsetY / this.zoom - ev.offsetY / prev_zoom
      );
      this.draw();
    },
  },
  mounted() {
    this.canvas = this.$refs.canvas;
    this.canvas.width = this.width;
    this.canvas.height = this.height;
    this.ctx = this.canvas.getContext("2d");
    this.calc_and_apply_base_values();
    this.load_map_and_draw();
  },
};
</script>

<style scoped>
canvas {
  border: 1px solid;
}
</style>
