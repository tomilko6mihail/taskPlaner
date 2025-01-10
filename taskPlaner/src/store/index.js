import {createStore} from 'vuex'
export default createStore({
    state: {
        tasks: [
            {id: 1, statusId: 0, title: "Вытереть жопу", responsible: "Юра Гарифулин"},
            {id: 2, statusId: 0, title: "Вытереть окно", responsible: "Витя Мамонтов"},
            {id: 3, statusId: 1, title: "Пройти Miside и отсосать у бомжа", responsible: ""},
            {id: 4, statusId: 2, title: "Ошибиться при выборе вуза", responsible: "Впр 11"}
        ]
    },
    mutations: {
        deleteTask(state, idTask){
            state.tasks = state.tasks.filter(x => x.id !== idTask)
        },
        addTask(){

        }
    }
})