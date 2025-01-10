<template>
  <div class="app">
    <headerComponent/>
    <main>
      <TaskColumn :statusId="0" :url-image="'/src/assets/img/task-square.svg'" :name-column="'Бэклог'"></TaskColumn>
      <TaskColumn :statusId="1" :url-image="'/src/assets/img/clock.svg'" :name-column="'В процессе'" style="margin-inline: 40px;"></TaskColumn>
      <TaskColumn :statusId="2" :url-image="'/src/assets/img/tick-circle.svg'" :name-column="'Выполнено'"></TaskColumn>
    </main>
  </div>
</template>

<script>
import headerComponent from './components/headerComponent.vue';
import TaskColumn from './components/taskColumn.vue';
  export default {
    components: {
      headerComponent, TaskColumn
    },
  }
</script>

<style scoped>
.app{
  padding: 30px;
  background: white;
}
main {
  width: 100%;
  height: 80vh;
  display: flex;
}
</style>