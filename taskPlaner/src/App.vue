<template>
  <div class="app">
    <headerComponent/>
    <main>
      <TaskColumn :url-image="'/src/assets/img/task-square.svg'" :name-column="'Бэклог'"></TaskColumn>
      <TaskColumn :url-image="'/src/assets/img/clock.svg'" :name-column="'В процессе'" style="margin-inline: 40px;"></TaskColumn>
      <TaskColumn :url-image="'/src/assets/img/tick-circle.svg'" :name-column="'Выполнено'"></TaskColumn>
    </main>
  </div>
</template>

<script>
import headerComponent from './components/headerComponent.vue';
import TaskColumn from './components/taskColumn.vue';
  export default {
    components: {
      headerComponent, TaskColumn
    }
  }
</script>

<style>
*{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  text-decoration: none;
}
.app{
  padding: 30px;
  background: white;
}
main{
  width: 100%;
  height: 80vh;
  display: flex;
}
</style>