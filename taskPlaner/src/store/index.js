import { onUpdated } from 'vue'
import {createStore} from 'vuex'
export default createStore({
    state: {
        tasks: [
            {id: 0, statusId: 0, title: "Вытереть жопу", responsible: "Юра Гарифулин", description: "какой то наипиздатейший текст здесь"},
            {id: 1, statusId: 0, title: "Мазануть мимо", responsible: "Витя Мамонтов", description: "акой то наипиздатейший текст здесь"},
            {id: 2, statusId: 1, title: "Пройти Miside и жеско отсосать у вонючего бомжа", responsible: "", description: ""},
            {id: 3, statusId: 2, title: "Ошибиться при выборе вуза", responsible: "Впр 11", description: "акой то наипиздатейший текст здесь"},
            {id: 4, statusId: 2, title: "Ашибиться при выборе вуза", responsible: "Впр 11", description: "rакой то наипиздатейший текст здесь"}
        ],
        dragOutNative: 1,
        isShowDialog: false,
        currentDisplayTask: {id: 2, statusId: 1, title: "Пройти Miside и жеско отсосать у вонючего бомжа", responsible: "", description: ""},
        optionRenderModal: '',
        selectedSort: "title"
    },
    mutations: {
        deleteTask(state, idTask){
            state.tasks = state.tasks.filter(x => x.id !== idTask)
        },
        addTask(state, newTask){
            state.tasks.push(newTask)
        },
        setSelectedSort(state, sort){
            state.selectedSort = sort
        },
        editTask(state, editTask){
            let index = state.tasks.findIndex(x => x.id === editTask.id) // в массиве ищем индекс элемента, в котором хотим поменять статус айди
            state.tasks[index] = editTask //меняем статус айди
        },
        setIdStatusTask(state, params){
            let index = state.tasks.findIndex(x => x.id === parseInt(params[0])) // в массиве ищем индекс элемента, в котором хотим поменять статус айди
            state.tasks[index].statusId = parseInt(params[1]) //меняем статус айди
            state.dragOutNative = 1 // возвращаем в исходную позицию переключатель игнорирования первого захода элемента в контейнер (чтоб скрипт не срабатывал сразу как начинаю тянуть)
            
        },
        searchTask(state, searchText){
            state.tasks.filter(x => x.title.toLowerCase().includes(searchText.toLowerCase()))
            //console.log(state.tasks);
        },
        toggleDialog(state){
            state.isShowDialog = !state.isShowDialog
        },
        setCurrentDisplayTask(state, task){
            state.currentDisplayTask = task
        },
        setOptionRenderModal(state, option){
            state.optionRenderModal = option
        }
    }
})