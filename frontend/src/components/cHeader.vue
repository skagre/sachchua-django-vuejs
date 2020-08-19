<template lang="pug">
    .header
        router-link(:to="{ path: '/' }") 
            img(class="logo" src="@/assets/images/logo.png", alt="logo")
            h1.logo-text Sách chùa
        div.search-form
            input(type="text", placeholder="Tìm kiếm...", v-model="search")
            button(type="submit", v-on:click="searchBook()")
                i.fas.fa-search
</template>

<script>

export default {

}
</script>

<style>

</style>