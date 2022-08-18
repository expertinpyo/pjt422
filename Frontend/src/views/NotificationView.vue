<template>
  <div class="notifications-container">
    <div class="notification-label">
      <img
        src="@/assets/notification.png"
        width="35"
        weight="35"
        class="notification-label-icon"
      />
      새로운 알림이 있습니다
    </div>
    <div
      v-for="notification in notifications"
      :key="notification.id"
      class="notification alert fade show"
      :class="{
        'alert-warning': notification.status === 'CAU',
        'alert-danger': notification.status === 'WAR',
      }"
      role="alert"
    >
      <span class="notification-left">
        <strong>{{ notification.token }}</strong>
        ({{ notification.location_x }}, {{ notification.location_y }})
        {{ (100 * notification.current_amount) / notification.total_amount }}%
      </span>
      <span class="notification-center">
        내용내용내용내용내용내용내용내용내용내용내용내용
      </span>
      <span class="notification-right">
        <img class="notification-alarm-img" src="@/assets/alarm.png" />
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "NotificationView",
  computed: {
    notifications() {
      return this.$store.state.notifications;
    },
  },
  async created() {
    try {
      await this.$store.dispatch("getNotifications");
    } catch (err) {
      //
    }
  },
};
</script>

<style scoped>
.notifications-container {
  width: 80%;
  margin: 100px auto;
  padding: 50px;
  background-color: #fafafa;
  border-radius: 20px;
}
.notification {
  display: flex;
}
.notification-alarm-img {
  width: 20px;
}
.notification-left {
  margin-right: auto;
}
.notification-right {
  margin-left: auto;
}
.notification-label {
  margin: 70px 0;
  font-weight: bolder;
  font-size: 25px;
  color: #292929;
}
.notification-label img {
  margin-right: 10px;
}
</style>
