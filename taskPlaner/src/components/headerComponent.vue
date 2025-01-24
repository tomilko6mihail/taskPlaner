<template>
    <header>
        <div style="display: flex; align-items: center;">
            <img src="../assets/img/scroll.svg" height="30" width="30" style="margin-right: 10px;" alt="logo">
            <h1>Планеровщик задач</h1>
        </div>
        <div style="display: flex; align-items: center; position: relative;">
            <div :class="toggleFilter == true ? 'filter-comp' : 'filter-comp filter-hide'">
                <div class="filter-left"></div>
                <div class="filter">
                    <h2>Сортировать по:</h2>
                    <div class="radio-input">
                        <div style="display: flex;">
                            <input checked="" id="radio1" class="input" @click="$store.commit('setSelectedSort', 'title')" type="radio" name="radio">
                            <label for="radio1">Заголовку</label>
                        </div>
                        <div style="display: flex;">
                            <input @click="$store.commit('setSelectedSort', 'description')" class="input" id="radio2" type="radio" name="radio">
                            <label for="radio2">Содержимому</label>
                        </div>
                        <div style="display: flex;">
                            <input @click="$store.commit('setSelectedSort', 'responsible')" class="input" id="radio3" type="radio" name="radio">
                            <label for="radio3">Ответственному</label>
                        </div>
                    </div>
                </div>
                <div class="filter-right"></div>

            </div>
            <input @input="updateInput" placeholder="Поиск..." type="text">
            <a @click="toggleFilter = !toggleFilter" role="button" style="cursor: pointer;"><img src="../assets/img/sort.svg" alt="filter"></a>
            <button @click="$store.commit('setOptionRenderModal', 'profile'), $store.commit('toggleDialog')" class="user__btn"><img src="../assets/img/user-square.svg" alt="user-square"></button>
        </div>
    </header>
</template>

<script>
import store from '@/store';

export default {
    methods: {
        updateInput(event) {
            this.$emit("update:modelValue", event.target.value)
        }
    },
    data() {
        return {
            toggleFilter: false
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
    font-family: gothambook;
    src: url(../assets/fonts/gotham_book.otf);
}

@font-face {
    font-family: gothammedium;
    src: url(../assets/fonts/gotham_medium.otf);
}
@media (max-width: 715px){
    header{
        height: auto;
    }
    header h1 {
    width: 50%;
    font-size: 15px;
    margin-right: 50px;
}
.filter-comp{
    bottom: -291%!important;
}
}
@media (max-width: 670px){
    header h1 {
        display: none;
        margin: 0;
}
.filter-comp{
        bottom: -349%!important;
        
    }
}
@media (max-width: 520px){
    header div img[alt="logo"]{
        display: none;
    }
    header{
        justify-content: center!important;
    }
    .filter-comp{
        left: -5%!important;
        bottom: -349%!important;
        
    }
}
@media (max-width: 390px){
    header div img[alt="logo"]{
        display: none;
    }
    header{
        justify-content: center!important;
    }
    input[type="text"]{
        width: 100%!important;
    }
    .filter-comp{
        left: -5%!important;
        bottom: -343%!important;
    }
}

h2 {
    font-family: gothammedium;
    color: white;
    font-size: 18px;
    margin-bottom: 5px;
}

label {
    font-family: gothambook;
    color: white;
    font-size: 15px;
}
.filter{
    background: black;
    border-radius: 0 0 10px 10px;
    width: 100%;
    padding: 18px;
}
.filter-comp {
    position: absolute;
    display: grid;
    grid: 100% / 6% 88% 6%;
    width: 110%;
    height: auto;
    z-index: 1;
    left: -11%;
    bottom: -348%;
    transform: rotateX(0deg);
    transform-origin: top;
    filter: drop-shadow(2px 2px 8px rgba(0, 0, 0, .4));
    transition: all 0.15s linear;
}
.filter-hide {
    transform: rotateX(90deg);
    filter: drop-shadow(0px 0px 0px rgba(0, 0, 0, .4));
    transition: all 0.15s linear;
}

.filter-left{
    background: url(../assets/img/filter-l-r.svg);
    background-size: 100%;
    background-position-x: 1px;
    background-position-y: top;
    background-repeat: no-repeat;
}
.filter-right{
    background: url(../assets/img/filter-l-r.svg);
    background-size: 100%;
    background-position-x: 0px;
    background-position-y: top;
    background-repeat: no-repeat;
    transform: rotateY(180deg);
    position: relative;
    left: -1px;
}

.radio-input div {
    display: flex;
    align-items: center;
}

header {
    background: #05050D;
    border-radius: 100px;
    padding: 10px 30px;
    display: flex;
    justify-content: space-between;
    flex-wrap: nowrap;
    width: 100%;
    min-height: 70px;
    margin-bottom: 30px;
    position: relative;
    z-index: 2;
}

a {
    display: flex;
    margin-inline: 10px;
}

header h1 {
    color: white;
    font-family: gothamlight;
    font-size: 25px;
}

input[type="text"] {
    height: 30px;
    width: 200px;
    border-radius: 7px;
    border: none;
    padding: 5px;
    padding-left: 26px;
    background: url(../assets/img/search-normal.svg);
    background-repeat: no-repeat;
    background-size: 15px;
    background-position-x: 6px;
    background-position-y: 6px;
    outline: none;
    position: relative;
    top: 0;
    background-color: white;
    font-family: gothambook;
    transition: all 0.2s ease-in-out;
}

input[type="text"]::placeholder {
    font-family: gothambook;
}
input[type="text"]:focus{
    top: -2px;
    box-shadow: 0px 2px 0px 0px rgb(180, 180, 180);
    transition: all 0.2s ease-in-out;
}

.user__btn {
    height: 30px;
    width: 30px;
    padding: 5px;
    background: #9379F2;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
}

.input {
    -webkit-appearance: none;
    padding: 0;
    display: block;
    margin: 8px;
    width: 18px;
    height: 18px;
    border-radius: 12px;
    cursor: pointer;
    vertical-align: middle;
    background-color: hsl(0, 0%, 100%);
    background-image: -webkit-radial-gradient(hsl(253, 82%, 71%) 0%, hsl(253, 82%, 71%) 35%, hsla(253, 82%, 71%, 0) 36%, hsla(253, 96%, 47%, 0) 100%);
    background-repeat: no-repeat;
    background-size: 100%;
    -webkit-transition: background-position .15s cubic-bezier(.8, 0, 1, 1),
        -webkit-transform .15s cubic-bezier(.8, 0, 1, 1);
    outline: none;
}

.input:checked {
    -webkit-transition: background-position .2s .15s cubic-bezier(0, 0, .2, 1),
        -webkit-transform .15s cubic-bezier(0, 0, .2, 1);
}

.input:active {
    -webkit-transform: scale(1.2);
    -webkit-transition: -webkit-transform .1s cubic-bezier(0, 0, .2, 1);
}
.input,
.input:active {
    background-position: 0 20px;
}

.input:checked {
    background-position: 0 0;
}

.input:checked~.input,
.input:checked~.input:active {
    background-position: 0 -20px;
}
</style>