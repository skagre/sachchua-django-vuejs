<template lang="pug">
    .container
        //- header
        cHeader
        //-end header


        //- detail
        .detail-sidebar
            div(style="background-color: #fff; padding: 20px 0; border-top: 3px solid #27AB83;")
                .book-detail
                    img(v-bind:src="book.thumbnail", alt="alt")
                    h1 {{ book.title }}
                    p 
                        i.fas.fa-user-tag  
                        | {{ book.author }}
                    p {{ book.category_name }}
                .book-links
                    a(v-bind:href="book.file", target="_blank")
                        i.fas.fa-eye
                        | Đọc online
                    router-link(:to="{ path: '/' }")
                        i.fas.fa-home
                        | Về trang chủ
        .detail-content
            .detail-content__book-detail
                img(v-bind:src="book.thumbnail", alt="alt")
                div
                    h1 {{ book.title }}
                    p {{ book.author }}
            .detail-content__heding
                h2 Nội dung:
            .detail-content__book-content
                p {{ book.content }}
            .detail-content__heding
                h2 Tải xuống:
            a(v-bind:href="book.file" class="detail-content__book-download", target="_blank")
                i.fas.fa-download PDF
                span {{ book.title }}
            .detail-content__heding
                h2 Bình luận:
            div(class="fb-comments" data-href="http://127.0.0.1:808/#/" data-numposts="5" data-width="100%" data-lazy="true")
            #fb-root
            script(type="application/javascript" async defer crossorigin="anonymous" src="https://connect.facebook.net/vi_VN/sdk.js#xfbml=1&version=v7.0" nonce="WFcY15E0")
        //- end detail


        //- footer
        cFooter
        //- end footer
    
</template>

<script>
import cHeader from '@/components/cHeader.vue'
import cFooter from '@/components/cFooter.vue'

import axios from 'axios'

export default {
    name: 'Detail',
    components: {
        cHeader,
        cFooter,
    },
    data() {
        return {
            base_url: `http://localhost:8000/`,
            book: null,
        }
    },
    created() {
        this.getBookByID();
    },
    watch: {
        '$route': 'getBookByID'
    },
    methods: {
        getBookByID() {
            axios.get(this.base_url + `api/book/` + this.$route.params.id)
            .then((res) => {
                this.book = res.data;
            });
        },
    },
}
</script>

<style>

</style>