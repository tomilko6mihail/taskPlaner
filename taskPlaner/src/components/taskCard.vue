<template>
    <article :id="`${task.id.toString()}i`" :class="task.id.toString()">
        <div :class="(isFakeCardShow ? 'fake-card active' : 'fake-card')"></div>
        <div v-on:mouseover="isFakeCardShow = true" v-on:mouseout="isFakeCardShow = false" class="card">
            <header>
                <div v-if="screen > 975" class="drag-n-drop-btn"></div>
            </header>
            <main>
                <label>Название:</label>
                <h3>{{ task.title }}</h3>
                <label>Ответственный:</label>
                <p>{{ task.responsible === "" ? 'Не назначен' : task.responsible }}</p>
                <div class="two-btns">
                    <button @click="$store.commit('setOptionRenderModal', 'viewTask'), $store.commit('setCurrentDisplayTask', task), $store.commit('toggleDialog')" class="violet"><img src="../assets/img/setting.svg" alt="params">Параметры</button>
                    <button @click="$store.commit('deleteTask', task.id)" class="red" style="border-color: #ef4c4c; width: 46px; margin-left: 10px;"><img
                            src="../assets/img/trash.svg" alt="" style="margin: 0;"></button>
                </div>
            </main>
        </div>
    </article>

</template>

<script>
export default {
    props: {
        task: {
            type: Object,
            required: true
        }
    },
    data(){
        return {
            isFakeCardShow: false,
            screen: window.innerWidth
        }
    }
}
</script>

<style scoped>
@font-face {
    font-family: gothamlight;
    src: url(../assets/fonts/gotham_light.otf);
}

@font-face {
    font-family: gothambold;
    src: url(../assets/fonts/gotham_bold.otf);
}

@font-face {
    font-family: gothambook;
    src: url(../assets/fonts/gotham_book.otf);
}

@font-face {
    font-family: gothammedium;
    src: url(../assets/fonts/gotham_medium.otf);
}

.two-btns {
    display: flex;
    justify-content: space-between;
}

.fake-card {
    width: 100%;
    height: 100%;
    position: absolute;
    background: #b598eb;
    z-index: 1;
    border-radius: 10px 10px 10px 10px;
    left: 0;
    transition: all 0.15s ease-in-out;
}
.active{
    border-radius: 8px 10px 10px 8px;
    left: -5px;
    transition: all 0.15s ease-in-out;
}
button {
    border: 2px solid #925FF0;
    border-radius: 5px;
    width: 100%;
    height: 36px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: gothammedium;
    color: #925FF0;
    background: none;
    padding: 5px;
    box-shadow: inset 0 0 0 0 white;
    transition: all 0.15s ease-in-out;
}

.violet:hover {
    box-shadow: inset 7px -7px 6px -5px #c8baff;
    transition: all 0.15s ease-in-out;
}

.red:hover {
    box-shadow: inset 7px -7px 6px -5px #ffbaba;
    transition: all 0.15s ease-in-out;
}

button img {
    margin-right: 8px;
}

.drag-n-drop-btn {
    display: flex;
    justify-content: center;
    align-items: center;
    background: white;
    background-image: url(../assets/img/drag-icon.svg);
    background-position: center;
    background-repeat: no-repeat;
    height: 20px;
    width: 35px;
    color: white;
    border-radius: 0 10px 0 10px;
    box-shadow: inset 2px -1px 5px 0px #00000017;
    cursor: move;
}

header {
    height: 20px;
    width: 100%;
    display: flex;
    justify-content: end;
}
article{
    width: 100%;
    margin-bottom: 30px;
    height: auto;
    position: relative;
}
article .card {
    width: 100%;
    height: auto;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0px 5px 5px rgb(0 0 0 / 10%);
    display: flex;
    z-index: 1;
    position: relative;
    flex-direction: column;
    transition: all 0.15s ease-in-out;
}

article .card:hover {
    box-shadow: 0px 5px 8px rgba(47, 12, 60, 0.15);
    transition: all 0.15s ease-in-out;
}

main {
    padding: 20px;
    display: flex;
    flex-direction: column;
    padding-top: 0px;
}

label {
    font-family: gothamlight;
    font-size: 13px;
}

h3 {
    font-family: gothambold;
    margin-bottom: 20px;
}

p {
    margin-bottom: 15px;
    font-family: gothambook;
}
</style>