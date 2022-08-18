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
        <strong>
          {{ notification.floor.building.name }} {{ notification.floor.name }}층
          ({{ notification.location_x }}, {{ notification.location_y }}) 위치의
          쓰레기통
        </strong>
      </span>
      <span v-if="notification.amount >= 0.7">
        <strong>위험! 해당 쓰레기통을 지금 바로 비워주세요!</strong>
      </span>
      <span v-else>
        <strong>
          주의! 해당 쓰레기통은 현재
          {{ Number(notification.amount * 100).toFixed(1) }}% 만큼 차있습니다.
        </strong>
      </span>

      <span></span>
      <span class="notification-center"></span>
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
