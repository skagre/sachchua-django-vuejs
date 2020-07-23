<template lang="pug">
    .header
        router-link(:to="{ path: '/' }") 
            img(class="logo" src="https://image.flaticon.com/icons/svg/2232/2232688.svg", alt="logo")
            h1.logo-text Sách chùa
        form.search-form(action="", method="POST")
            input(type="text", placeholder="Tìm kiếm...")
            button(type="submit")
                i.fas.fa-search
</template>

<script>
export default {

}
</script>

<style>

</style>