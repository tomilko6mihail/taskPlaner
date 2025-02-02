import { onUpdated } from "vue";
import { createStore } from "vuex";
import axios from 'axios'

export default createStore({
  state: {
    tasks: [
      {
        id: 0,
        statusId: 0,
        title: "Моя работа для портфолио",
        responsible: "Михаил томилко",
        description: "",
      },
      {
        id: 4,
        statusId: 0,
        title: "Весь текст не более чем наполнитель",
        responsible: "Михаил Томилко",
        description: "Какой то доп текст",
      },
      {
        id: 1,
        statusId: 1,
        title: "Этот проект находится в разработке",
        responsible: "Михаил Томилко",
        description: "Что грядет: система регистрации и входа в аккаунт, отображение только тех задач, которые привязаны к аккаунту + команды(если пользователь ввел код команды), система совместного проектирования(как раз команда), возможность назначения админа в команде, возможность стилизации текста внутри описания",
      },
      {
        id: 2,
        statusId: 1,
        title: "Опустошить холодильник в 4 ночи",
        responsible: "Иван Гамаз",
        description: "Ну тут тоже какой нибудь дополнительный скучный текст",
      },
      {
        id: 3,
        statusId: 2,
        title: "Ошибиться при выборе вуза",
        responsible: "ВПР 11",
        description: "",
      },
    ],
    dragOutNative: 1,
    isShowDialog: false,
    currentDisplayTask: {
      id: 2,
      statusId: 1,
      title: "",
      responsible: "",
      description: "",
    },
    optionRenderModal: "",
    selectedSort: "title",
  },
  mutations: {
    deleteTask(state, idTask) {
      state.tasks = state.tasks.filter((x) => x.id !== idTask);
    },
    addTask(state, newTask) {
      state.tasks.push(newTask);
    },
    setSelectedSort(state, sort) {
      state.selectedSort = sort;
    },
    editTask(state, editTask) {
      let index = state.tasks.findIndex((x) => x.id === editTask.id); // в массиве ищем индекс элемента, в котором хотим поменять статус айди
      state.tasks[index] = editTask; //меняем статус айди
    },
    setIdStatusTask(state, params) {
      let index = state.tasks.findIndex((x) => x.id === parseInt(params[0])); // в массиве ищем индекс элемента, в котором хотим поменять статус айди
      state.tasks[index].statusId = parseInt(params[1]); //меняем статус айди
      state.dragOutNative = 1; // возвращаем в исходную позицию переключатель игнорирования первого захода элемента в контейнер (чтоб скрипт не срабатывал сразу как начинаю тянуть)
    },
    searchTask(state, searchText) {
      state.tasks.filter((x) =>
        x.title.toLowerCase().includes(searchText.toLowerCase())
      );
      //console.log(state.tasks);
    },
    toggleDialog(state) {
      state.isShowDialog = !state.isShowDialog;
    },
    setCurrentDisplayTask(state, task) {
      state.currentDisplayTask = task;
    },
    setOptionRenderModal(state, option) {
      state.optionRenderModal = option;
    },
  },
  actions: {
    async fetchTasks() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/tasks");
        console.log(response.data)
      } catch (e) {
        console.log(e)
        //alert("Error server");
      } finally {
        console.log('end fetch')
      }
    },
    async loginUser() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/login', {
            email: 'penis@yadenx.ru',
            password: 'huilo228'
          }
        )
        console.log(response.data)
      } catch (e) {
        console.log(e)
        //alert("Error server");
      } finally {
        console.log('end fetch')
      }
    },
  },
});
