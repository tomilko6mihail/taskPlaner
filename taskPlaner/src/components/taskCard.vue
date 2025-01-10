<template>
    <article>
        <header>
            <div class="drag-n-drop-btn"></div>
        </header>
        <div class="card">
            <label>Название:</label>
            <h3>{{ task.title }}</h3>
            <label>Ответственный:</label>
            <p>{{ task.responsible }}</p>
            <div class="two-btns">
                <button><img src="../assets/img/setting.svg" alt="">Параметры</button>
                <button style="border-color: #E42E2E; width: 46px; margin-left: 10px;"><img src="../assets/img/trash.svg" alt="" style="margin: 0;"></button>
            </div>
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
.two-btns{
    display: flex;
    justify-content: space-between;
}
button{
    border: 2px solid #925FF0;
    border-radius: 5px;
    width: 100%;
    height: 36px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: gothambook;
    color: #925FF0;
    background: none;
    padding: 5px;
}
button img {
    margin-right: 8px;
}
.drag-n-drop-btn{
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
header{
    height: 20px; 
    width: 100%;
    display: flex;
    justify-content: end;
}
article {
    width: 100%;
    height: auto;
    background-color: white;
    border-radius: 10px;
    margin-bottom: 30px;
    box-shadow: 0px 5px 5px rgb(0 0 0 / 3%);
    display: flex;
    flex-direction: column;

}
.card{
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