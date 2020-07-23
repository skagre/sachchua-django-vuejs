<template lang="pug">
    .container
        //- header
        cHeader
        //-end header
        

        //- content
        .content
            .text-heading
                img(src="https://image.flaticon.com/icons/svg/3100/3100752.svg", alt="text-heading")
                h3 Sách mới cập nhật
                
            router-link(:to="{ path: '/detail/' + book.id }", class="book", v-for="book in books.books", :key="book.id")
                img(v-bind:src="book.thumbnail", alt="thumbnail")
                .book__overlay
                    i.fas.fa-compress-alt
                .book__effect
                p.book__category {{ book.category_name }}
                p.book__title {{ book.title }}
                p.book__author 
                    i.fas.fa-user-tag 
                    | {{ book.author }}
        //- end content


        //- sidebar
        .sidebar
            div(style="background-color: #fff; border-radius: 12px; padding: 25px;")
                .text-heading
                    img(src="https://image.flaticon.com/icons/svg/3100/3100752.svg", alt="text-heading")
                    h3 Thể loại sách
                ul
                    li(v-for="category in categories", v-bind:key="category.id")
                        router-link(:to="{ path: '/category/' + category.id }") 
                            i.far.fa-folder-open 
                            | {{ category.name }}
        //- end sidebar


        //- footer
        cFooter
        //- end footer
</template>

<script>
// @ is an alias to /src
import cHeader from '@/components/cHeader.vue'
import cFooter from '@/components/cFooter.vue'

import axios from 'axios'

export default {
    name: 'Home',
        components: {
        cHeader,
        cFooter,
    },
    data() {
        return {
            base_url: `http://localhost:8000/`,
            books: null,
            categories: null,
        }
    },
    created()  {
        this.getAllCategory();
        this.getBookByCategoryID();
    },
    watch: {
        '$route': 'getBookByCategoryID'
    },
    methods: {
        getBookByCategoryID() {
            axios.get(this.base_url + `api/category/${this.$route.params.id}`)
            .then((res) => {
                this.books = res.data;
            });
        },
        getAllCategory() {
            axios.get(this.base_url + `api/category/`)
            .then((res) => {
                this.categories = res.data;
            });
        },
    },
}
</script>
