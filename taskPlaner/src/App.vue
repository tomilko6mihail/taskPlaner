<template>
  <div class="app">
    <headerComponent v-model="search" />
    <main class="">
      <TaskColumn :tasks="searchTasks" :statusId="0" :url-image="'/src/assets/img/task-square.svg'" :name-column="'Бэклог'"></TaskColumn>
      <TaskColumn :tasks="searchTasks" :statusId="1" :url-image="'/src/assets/img/clock.svg'" :name-column="'В процессе'"
        style="margin-inline: 40px;"></TaskColumn>
      <TaskColumn :tasks="searchTasks" :statusId="2" :url-image="'/src/assets/img/tick-circle.svg'" :name-column="'Выполнено'"></TaskColumn>
    </main>
  </div>
</template>

<script>
import headerComponent from './components/headerComponent.vue';
import TaskColumn from './components/taskColumn.vue';
import store from './store';
export default {
  components: {
    headerComponent, TaskColumn
  },
  data(){
    return {
      search: ""
      //tasks: store.state.tasks
    }
  },
  mounted() {
    dragula([
      document.getElementById(0),
      document.getElementById(1),
      document.getElementById(2),
    ], {
      accepts: function (el, target, source, sibling) {
        return true; // по умолчанию элементы могут быть помещены в любой из `контейнеров`
      }
    }).on('drop', function (el, target) {
      store.commit('setIdStatusTask', [el.className[0], target.id]) //мутируем стейт, передавая айдишник дропнутого айтема и айдишник куда дропнулся контейнер(далее см в store)
    })
  },
  computed: {
    searchTasks(){
      return store.state.tasks.filter(task => task.title.toLowerCase().includes(this.search.toLowerCase()))
    }
  }
}
</script>

<style scoped>
.app {
  padding: 30px;
  background: white;
}

main {
  width: 100%;
  height: 80vh;
  display: flex;
}
</style>