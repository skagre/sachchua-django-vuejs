<template lang="pug">
    .header
        router-link(:to="{ path: '/' }") 
            img(class="logo" src="@/assets/images/logo.png", alt="logo")
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