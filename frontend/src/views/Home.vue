<template lang="pug">
  .container

    .header
      router-link(:to="{ path: '/' }") 
          img(class="logo" src="@/assets/images/logo.png", alt="logo")
          h1.logo-text Sách chùa
      div.search-form
          input(type="text", placeholder="Tìm kiếm...", v-model="search")
          button(type="submit", v-on:click="searchBook()")
              i.fas.fa-search

    .content
      .text-heading
        img(src="@/assets/images/books.png", alt="text-heading")
        h3 Sách mới cập nhật

      p(v-if="books.length == 0") Không có dữ liệu

      router-link(:to="{ path: '/detail/' + book.id }", class="book", v-for="book in books", :key="book.id")
        img(v-bind:src="book.thumbnail", alt="thumbnail")
        .book__overlay
          i.fas.fa-compress-alt
        .book__effect
        p.book__category {{ book.category_name }}
        p.book__title {{ book.title }}
        p.book__author 
          i.fas.fa-user-tag 
          | {{ book.author }}

    .sidebar
      div(style="background-color: #fff; border-radius: 12px; padding: 25px;")
        .text-heading
          img(src="@/assets/images/categories.png", alt="text-heading")
          h3 Thể loại sách
        ul
          li(v-for="category in categories", v-bind:key="category.id")
            router-link(:to="{ path: '/category/' + category.id }") 
              i.far.fa-folder-open 
              | {{ category.name }}

    cFooter
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
      search: ''
    }
  },
  created() {
    this.getAllBook();
    this.getAllCategory();
  },
  methods: {
    getAllBook() {
      axios.get(this.base_url + `api/book/?limit=100`)
      .then((res) => {
        this.books = res.data.results;
      })
      .catch((err) => {
        alert(JSON.stringify(err.response.data, null, 4));
      });
    },
    getAllCategory() {
      axios.get(this.base_url + `api/category/?limit=100`)
      .then((res) => {
        this.categories = res.data.results;
      })
      .catch((err) => {
        alert(JSON.stringify(err.response.data, null, 4));
      });
    },
    searchBook() {
      axios.get(this.base_url + `api/book/?search=` + this.search)
      .then((res) => {
          this.books = res.data.results;
      })
      .catch((err) => {
          alert(JSON.stringify(err.response.data, null, 4));
      });
    }
  },
}
</script>
