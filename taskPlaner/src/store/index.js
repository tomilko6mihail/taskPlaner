import {createStore} from 'vuex'
export default createStore({
    state: {
        tasks: [
            {id: 0, statusId: 0, title: "Вытереть жопу", responsible: "Юра Гарифулин"},
            {id: 1, statusId: 0, title: "Мазануть мимо", responsible: "Витя Мамонтов"},
            {id: 2, statusId: 1, title: "Пройти Miside и отсосать у бомжа", responsible: ""},
            {id: 3, statusId: 2, title: "Ошибиться при выборе вуза", responsible: "Впр 11"}
        ],
        dragOutNative: 1
    },
    mutations: {
        deleteTask(state, idTask){
            state.tasks = state.tasks.filter(x => x.id !== idTask)
            console.log(state.tasks);
            
        },
        addTask(){

        },
        setIdStatusTask(state, params){
            let index = state.tasks.findIndex(x => x.id === parseInt(params[0])) // в массиве ищем индекс элемента, в котором хотим поменять статус айди
            state.tasks[index].statusId = parseInt(params[1]) //меняем статус айди
            state.dragOutNative = 1 // возвращаем в исходную позицию переключатель игнорирования первого захода элемента в контейнер (чтоб скрипт не срабатывал сразу как начинаю тянуть)
        },
        searchTask(state, searchText){
            state.tasks.filter(x => x.title.toLowerCase().includes(searchText.toLowerCase()))
            console.log(state.tasks);
            
        }
    }
})