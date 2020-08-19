<template lang="pug">
    .category-container
        .category-heading
            h2 Quản lý thể loại
        .category-content
            .left
                .list-category
                    span.col1 ID
                    span.col2 Tên thể loại
                    span.col3 Số lượng sách
                    span.col4 Hành động
                p(v-if="categories.length == 0", style="margin-top: 30px; color: red; font-weight: bold;") Không có sách, hãy thêm mới !
                div(v-for="category in categories", :key="category.id")
                    .list-category(style="padding: 20px 0;") 
                        span.col.col1 \#{{ category.id }}
                        span.col.col2 {{ category.name }}
                            
                        span.col.col3 {{ category.books.length }}
                        span.col.col4
                            a(v-on:click="getCategoryName(category.id, category.name)") Sửa
                            a(v-on:click="deleteCategory(category.id)") Xóa
                        span.col.col5 Đăng bởi: {{ category.created_by }} 
                            p Ngày: {{ category.created_on }}
                        span.col.col6 Cập nhật bởi: 
                            span(v-if="category.user_updated == null") --- 
                                p Ngày: ---
                            span(v-else) {{ category.user_updated }} 
                                p Ngày: {{ category.updated_on }}
            
                .pagination
                    ul
                        li(v-for="i in Math.ceil(count / 5)")
                            button(v-on:click="loadCategories((i-1)*5)") {{ i }}
            .right
                h4 THÊM MỚI
                .input-group
                    input(type="text", placeholder="Tên thể loại", v-model="category_name")
                    button(v-on:click="addCategory()") Thêm
                h4 SỬA
                .input-group
                    input(type="text", placeholder="Tên thể loại", v-model="edit_category_name", v-bind:disabled="disabledEdit")
                    button(v-on:click="editCategory()") Sửa
</template>

<script>
import axios from 'axios'
export default {
    name: 'DashboardCategories',
    data() {
        return {
            base_url: `http://localhost:8000/`,
            categories: null,
            count: 0,

            category_name: '',
            edit_category_name: '',
            categoryID: '',
            disabledEdit: true
        }
    },
    created() {
        this.loadCategories();
    },
    methods: {
        loadCategories(offset = null) {
            axios({
                method: 'get',
                url: this.base_url + `api/category/?limit=5&offset=` + offset,
            })
            .then((res) => {
                this.categories = res.data.results;
                this.count = res.data.count;
            })
            .catch((err) => {
                alert(JSON.stringify(err.response.data, null, 4));
            });
        },
        addCategory() {
            axios({
                method: 'post',
                url: this.base_url + `api/category/`,
                data: {
                    'name': this.category_name,
                    'user': localStorage.getItem('id')
                },
                headers: {
                    'Authorization': localStorage.getItem('Authorization')
                }   
            })
            .then(() => {
                alert("Thêm mới thành công!");
                this.loadCategories();
            })
            .catch((err) => {
                alert(JSON.stringify(err.response.data, null, 4));
            });
        },
        deleteCategory(id) {
            if (confirm("Sẽ xóa toàn bộ sách trong thể loại này!\nBạn chắc chắn muốn xóa?"))
            {
                axios({
                    method: 'delete',
                    url: this.base_url + `api/category/` + id,
                    headers: {
                        'Authorization': localStorage.getItem('Authorization')
                    }   
                })
                .then(() => {
                    this.loadCategories();
                })
                .catch((err) => {
                    alert(JSON.stringify(err.response.data, null, 4));
                });
            }
        },
        getCategoryName(id, name) {
            this.edit_category_name = name;
            this.disabledEdit = false;
            this.categoryID = id;
        },
        editCategory() {
            if (confirm("Chấp nhận thay đổi?"))
            {
                axios({
                    method: 'patch',
                    url: this.base_url + `api/category/` + this.categoryID + '/',
                    data: {
                        'name': this.edit_category_name,
                    },
                    headers: {
                        'Authorization': localStorage.getItem('Authorization')
                    }   
                })
                .then(() => {
                    alert("Cập nhật thành công!");
                    this.disabledEdit = true;
                    this.loadCategories();
                })
                .catch((err) => {
                    alert(JSON.stringify(err.response.data, null, 4));
                });
            }
        }
    }
}
</script>

<style>

</style>