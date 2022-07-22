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
      offsetX: 0,
      offsetY: 0,
      mousePrevX: 0,
      mousePrevY: 0,
      currentMouseoverTrashbin: -1,
      currentTrashbin: -1,
    };
  },
  watch: {
    floor() {
      this.calcAndApplyBaseValues();
      this.loadMapAndDraw();
    },
    width() {
      this.canvas.width = this.width;
      this.canvas.height = this.height;
      this.calcAndApplyBaseValues();
      this.draw();
    },
  },
  methods: {
    draw() {
      this.ctx.resetTransform();
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
      this.ctx.scale(this.zoom, this.zoom);
      this.ctx.translate(this.offsetX, this.offsetY);

      this.ctx.drawImage(this.img, 0, 0);

      for (let trashbin of this.floor.trashbins) {
        this.ctx.save();
        this.ctx.fillStyle = trashbin.color;
        this.ctx.fillRect(
          trashbin.x - trashbin.size / 2,
          trashbin.y - trashbin.size / 2,
          trashbin.size,
          trashbin.size
        );

        this.ctx.lineWidth = 1;
        this.ctx.strokeStyle = "#000000";
        if (trashbin.hovered) {
          this.ctx.lineWidth = 2;
          this.ctx.strokeStyle = "#88FF88";
        }
        if (trashbin.selected) {
          this.ctx.lineWidth = 2;
          this.ctx.strokeStyle = "#FF8888";
        }
        this.ctx.strokeRect(
          trashbin.x - trashbin.size / 2,
          trashbin.y - trashbin.size / 2,
          trashbin.size,
          trashbin.size
        );
        this.ctx.restore();
      }
    },
    loadMapAndDraw() {
      this.img = new Image();
      this.img.onload = () => {
        this.draw();
      };
      this.img.src = this.floor.src;
    },
    calcAndApplyBaseValues() {
      this.baseZoom = Math.min(
        1,
        this.canvas.width / this.floor.width,
        this.canvas.height / this.floor.height
      );
      this.baseOffsetX = Math.max(
        0,
        (this.canvas.width / this.baseZoom - this.floor.width) / 2
      );
      this.baseOffsetY = Math.max(
        0,
        (this.canvas.height / this.baseZoom - this.floor.height) / 2
      );

      this.zoom = this.baseZoom;
      this.offsetX = this.baseOffsetX;
      this.offsetY = this.baseOffsetY;
    },
    changeZoom(zoomRatio) {
      if (this.zoom * zoomRatio < this.baseZoom * 0.75) {
        this.zoom = this.baseZoom * 0.75;
      } else if (this.zoom * zoomRatio > this.baseZoom * 4) {
        this.zoom = this.baseZoom * 4;
      } else {
        this.zoom *= zoomRatio;
      }
    },
    changeOffset(offsetXDelta, offsetYDelta) {
      this.offsetX += offsetXDelta;
      this.offsetY += offsetYDelta;
    },
    mousedown(ev) {
      if ((ev.buttons & 1) === 0) return;
      ev.stopPropagation();

      this.mousePrevX = ev.offsetX;
      this.mousePrevY = ev.offsetY;

      const canvasX = -this.offsetX + ev.offsetX / this.zoom;
      const canvasY = -this.offsetY + ev.offsetY / this.zoom;

      for (let trashbin of this.floor.trashbins) {
        const left = trashbin.x - trashbin.size / 2;
        const right = trashbin.x + trashbin.size / 2;
        const top = trashbin.y - trashbin.size / 2;
        const bottom = trashbin.y + trashbin.size / 2;

        if (
          canvasX > left &&
          canvasX < right &&
          canvasY > top &&
          canvasY < bottom
        ) {
          if (this.currentTrashbin == trashbin.id) {
            return;
          }
          if (this.currentTrashbin >= 0) {
            this.$emit("trashbinEvent", { type: "unselect" });
          }
          this.$emit("trashbinEvent", { type: "select", trashbin });
          this.currentTrashbin = trashbin.id;
          this.draw();
          return;
        }
      }
      if (this.currentTrashbin >= 0) {
        this.$emit("trashbinEvent", { type: "unselect" });
        this.currentTrashbin = -1;
        this.draw();
      }
    },
    mousemove(ev) {
      if ((ev.buttons & 1) === 1) {
        this.changeOffset(
          (ev.offsetX - this.mousePrevX) / this.zoom,
          (ev.offsetY - this.mousePrevY) / this.zoom
        );
        this.mousePrevX = ev.offsetX;
        this.mousePrevY = ev.offsetY;
        this.draw();
      }

      const canvasX = -this.offsetX + ev.offsetX / this.zoom;
      const canvasY = -this.offsetY + ev.offsetY / this.zoom;

      for (let trashbin of this.floor.trashbins) {
        const left = trashbin.x - trashbin.size / 2;
        const right = trashbin.x + trashbin.size / 2;
        const top = trashbin.y - trashbin.size / 2;
        const bottom = trashbin.y + trashbin.size / 2;

        if (
          canvasX > left &&
          canvasX < right &&
          canvasY > top &&
          canvasY < bottom
        ) {
          if (this.currentMouseoverTrashbin == trashbin.id) {
            return;
          }

          if (this.currentMouseoverTrashbin >= 0) {
            this.$emit("trashbinEvent", { type: "mouseout" });
          }
          this.$emit("trashbinEvent", { type: "mouseover", trashbin });
          this.currentMouseoverTrashbin = trashbin.id;
          this.draw();
          return;
        }
      }
      if (this.currentMouseoverTrashbin >= 0) {
        this.$emit("trashbinEvent", { type: "mouseout" });
        this.currentMouseoverTrashbin = -1;
        this.draw();
      }
    },
    wheel(ev) {
      const prevZoom = this.zoom;
      if (ev.deltaY < 0) this.changeZoom(1.1);
      else if (ev.deltaY > 0) this.changeZoom(1 / 1.1);
      this.changeOffset(
        ev.offsetX / this.zoom - ev.offsetX / prevZoom,
        ev.offsetY / this.zoom - ev.offsetY / prevZoom
      );
      this.draw();
    },
  },
  mounted() {
    this.canvas = this.$refs.canvas;
    this.canvas.width = this.width;
    this.canvas.height = this.height;
    this.ctx = this.canvas.getContext("2d");
    this.calcAndApplyBaseValues();
    this.loadMapAndDraw();
  },
};
</script>

<style scoped>
canvas {
  border: 1px solid;
}
</style>
