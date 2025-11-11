<template>
  <div class="app">
    <headerComponent v-model="search" />
    <main class="">
      <ModalWindow :optionRender="$store.state.optionRenderModal" v-if="$store.state.isShowDialog"></ModalWindow>
      <TaskColumn :selectedSort="selectedSort" :tasks="searchTasks" :statusId="0"
        :name-column="'Бэклог'"></TaskColumn>
      <TaskColumn :selectedSort="selectedSort" :tasks="searchTasks" :statusId="1"
         :name-column="'В процессе'"
        :style="screenWidth > 975 ? 'margin-inline: 40px;' : ''"></TaskColumn>
      <TaskColumn :selectedSort="selectedSort" :tasks="searchTasks" :statusId="2"
         :name-column="'Выполнено'"></TaskColumn>
    </main>
  </div>
</template>

<script>

// import dragula from 'dragula'; //включать при деплое
import headerComponent from './components/headerComponent.vue';
import TaskColumn from './components/taskColumn.vue';
import ModalWindow from './components/UI/modalWindow.vue';
import './lib/dragula.min.js' //включать при локальной разработке
import store from './store';
import { mapActions } from 'vuex';
export default {
  components: {
    headerComponent, TaskColumn
  },
  data() {
    return {
      search: "",
      screenWidth: window.innerWidth
    }
  },
  methods:{
    ...mapActions({
      fetchTasks: 'fetchTasks'
    })
  },
  mounted() {
    dragula([
      document.getElementById(0),
      document.getElementById(1),
      document.getElementById(2),
    ], {
      accepts: function (el, target, source, sibling) {
        return true; // по умолчанию элементы могут быть помещены в любой из `контейнеров`
      }, moves: function (el, source, handle, sibling) {
        if(window.innerWidth >= 975) return true
        else return false
      },
    }).on('drop', function (el, target) {
      store.commit('setIdStatusTask', [el.id.slice(0, -1), target.id]) //мутируем стейт, передавая айдишник дропнутого айтема и айдишник куда дропнулся контейнер(далее см в store)

    })
    this.fetchTasks()
  },
  computed: {
    searchTasks() {
      return store.state.tasks.filter(task => task.title.toLowerCase().includes(this.search.toLowerCase()))
    },
    selectedSort() {
      return store.state.selectedSort
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

@media (max-width: 975px) {
  main {
    height: auto;
    display: block;
  }
}
@media (max-width: 450px) {
  .app {
    padding: 15px!important;
  }
}
</style>
