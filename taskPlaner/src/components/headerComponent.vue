<template>
    <header>
        <div style="display: flex; align-items: center;">
            <img src="../assets/img/scroll.svg" height="30" width="30" style="margin-right: 10px;" alt="logo">
            <h1>Планеровщик задач</h1>
        </div>
        <div style="display: flex; align-items: center;">
            <a href=""><img src="../assets/img/sort.svg" alt="filter"></a>
            <input placeholder="Поиск..." type="text">
            <button class="user__btn"><img src="../assets/img/user-square.svg" alt="user-square"></button>
        </div>
    </header>
</template>

<script>
    export default {
        
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
header{
    background: #000000;
    border-radius: 100px;
    padding: 10px 30px;
    display: flex;
    justify-content: space-between;
    width: 100%;
    height: 70px;
    margin-bottom: 30px;
}
header h1{
    color: white;
    font-family: gothamlight;
    font-size: 25px;
}
input{
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
    background-color: white;
    font-family: gothambook;
    margin-inline: 10px;
}
input::placeholder{
    font-family: gothambook;
}
.user__btn{
    height: 30px;
    width: 30px;
    background: #925FF0;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
}
</style>