import {createStore} from 'vuex'
export default createStore({
    state: {
        tasks: [
            {id: 0, statusId: 0, title: "Вытереть жопу", responsible: "Юра Гарифулин"},
            {id: 1, statusId: 0, title: "Мазануть мимо", responsible: "Витя Мамонтов"},
            {id: 2, statusId: 1, title: "Пройти Miside и отсосать у бомжа", responsible: ""},
            {id: 3, statusId: 2, title: "Ошибиться при выборе вуза", responsible: "Впр 11"}
        ],
        columnsTriggers: {
            0: 2,
            1: 2,
            2: 2
        },
        dragOutNative: 1
    },
    mutations: {
        deleteTask(state, idTask){
            state.tasks = state.tasks.filter(x => x.id !== idTask)
        },
        addTask(){

        },
        setIdStatusTask(state, params){
            state.tasks[parseInt(params[0])].statusId = parseInt(params[1])
            state.dragOutNative = 1
        },
        setTriggerColumn(state, columnParams){
            state.dragOutNative += 1
            if(state.dragOutNative > 2){
                console.log(document.getElementById(0).childElementCount);
                console.log(document.getElementById(1).childElementCount);
                console.log(document.getElementById(2).childElementCount);
                state.columnsTriggers[0] = document.getElementById(0).childElementCount
                state.columnsTriggers[1] = document.getElementById(1).childElementCount
                state.columnsTriggers[2] = document.getElementById(2).childElementCount
                //state.columnsTriggers[columnParams[0]] = columnParams[1]
                //console.log(state.columnsTriggers[2])
                //console.log(columnParams.id, document.getElementById(columnParams.id).childElementCount)
            }
        }
    }
})