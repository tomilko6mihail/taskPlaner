<template>
    <div style="width: auto; height: auto;">
        <a role="button" :class="`${color} ${gotham}`">
        <slot></slot>
        </a>
    </div>
</template>

<script>
export default {
    name: 'MyLink',
    props: {
        color: {
            type: String,
            default: 'black'
        },
        gotham: {
            type: String,
            default: 'book'
        }
    }
}
</script>

<style scoped>
a{
    cursor: pointer;
    font-family: gothammedium;
    text-decoration: underline solid;
    text-underline-offset: 15px;
    transition: all 0.15s ease-in-out;
}
a:hover{
    text-decoration: underline solid;
    text-underline-offset: 3px;
    transition: all 0.15s ease-in-out;
}

.black{
    color: black;
    text-decoration-color: #764ac900;
}

.black:hover {
    color: var(--main-purple);
    text-decoration-color: var(--main-purple);
}

.purple{
    color: var(--main-purple);
    text-decoration-color: #764ac900;
}
.purple:hover {
    color: var(--main-purple);
    text-decoration-color: var(--main-purple);
}
.book{
    font-family: gothambook;
}
.medium{
    font-family: gothammedium;
}
</style>