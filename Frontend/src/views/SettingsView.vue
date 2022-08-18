<template>
  <div class="settings-container">
    <div class="page-selector">
      <RouterLink to="/settings/building" active-class="active">
        <button class="btn">건물 관리</button>
      </RouterLink>
      <RouterLink to="/settings/user" active-class="active">
        <button class="btn">사용자 목록</button>
      </RouterLink>
      <RouterLink to="/settings/manager" active-class="active">
        <button class="btn">관리자 목록</button>
      </RouterLink>
    </div>
    <div class="settings-page">
      <RouterView></RouterView>
    </div>
  </div>
</template>

<script>
export default {
  name: "SettingsView",
};
</script>

<style scoped>
.settings-container {
  display: flex;
  flex-direction: row;
}
.page-selector {
  display: flex;
  flex-direction: column;
  height: 600px;
  border-right: 1.5px solid #828282;
  padding: 10px;
  margin-right: 0;
}
.page-selector > a {
  margin: 20px 0;
}
.page-selector button {
  width: 120px;
}
.settings-page {
  width: 100%;
}
</style>
