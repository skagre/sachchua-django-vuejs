<template lang="pug">
    .dashboard
        h2 
            router-link(:to="{ path: '/' }") Sách chùa Admin Dashboard
        .admin-container
            .menu
                h4 Công cụ
                ul
                    li
                        router-link(:to="{ path: '/dashboard/profile' }")
                            i.fas.fa-user
                            | Hồ sơ cá nhân
                    li
                        router-link(:to="{ path: '/dashboard/books' }")
                            i.fas.fa-book
                            | Quản lý ebook
                    li
                        router-link(:to="{ path: '/dashboard/categories' }")
                            i.fas.fa-file-alt
                            | Quản lý thể loại
            .content
                .user
                    .user__avatar
                        img(src="@/assets/images/books.png", alt="alt")
                    .user__name 
                        | Xin chào, 
                        span {{ name }} 
                        | |
                    .user__logout
                        button(v-on:click="logout()") Đăng xuất
                router-view
        p(style="margin-top: 30px;") Made by 
            a(href="https://github.com/skagre/sachchua-django-vuejs", target="_blank") skagre
</template>

<script>

import axios from 'axios'
export default {
    name: 'Dashboard',
    data() {
        return {
            base_url: `http://localhost:8000/`,
            name: localStorage.getItem('name'),
        }
    },
    created() {
        this.checklogin();
    },
    methods: {
        checklogin() {
            axios({
                method: 'post',
                url: this.base_url + `api/checklogin/`,
                headers: {
                    'Authorization': localStorage.getItem('Authorization')
                }
            })
            .then((res) => {
                if(res.data.id == null) {
                    this.$router.push({ name: 'Login' }).catch(()=>{});
                }
            })
            .catch(() => {
                this.$router.push({ name: 'Login' }).catch(()=>{});
            })
        },
        logout() {
            localStorage.clear();
            this.$router.push({ name: 'Login' }).catch(()=>{});
        }
    },
}
</script>

<style>

</style>