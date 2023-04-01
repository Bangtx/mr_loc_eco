<template lang="pug">
  div
    .header-color
      v-list-item.pa-2.max-width.center
        v-img.hidden-sm-and-down(
          src="https://img.freepik.com/premium-vector/abstract-modern-ecommerce-logo-design-colorful-gradient-shopping-bag-logo-template_467913-995.jpg?w=2000"
          max-width="40"
        )
        v-spacer
        v-text-field.pa-0(
          label="Search"
          placeholder="product"
          hide-details
          background-color="white"
          height="40"
          solo
          prepend-inner-icon="mdi-home-search-outline"
        )
        v-spacer
        div.pa-2
          v-icon(color="white" ) mdi-home
          span.white--text.hidden-sm-and-down.font-size-12 Trang Chủ
        div.pa-2
          v-icon(color="white" ) mdi-account
          span.white--text.hidden-sm-and-down.font-size-12 Tài Khoản
        div
          v-btn(icon)
            v-icon(color="white" ) mdi-cart-outline
        div.hidden-md-and-up
          v-btn(icon @click="onShowCategory()")
            v-icon(color="white" ) mdi-menu
        //h1.white--text Home page

      v-divider(color="white")
      .pc.category.max-width.center.hidden-sm-and-down
        ul
          li.pa-2.white--text(v-for="categoryTop in categoriesTop" @click="gotoProductsPage(categoryTop)")
            span.font-size-12 {{ categoryTop.name }}
      .center.hidden-md-and-up
        v-expand-transition
          v-card(
            color="#f57e2e"
            v-show="isShowCategoryInMobile"
            class="mx-auto"
          )
            ul
              li.pa-2.white--text(v-for="categoryTop in categoriesTop" @click="gotoProductsPage(categoryTop)")
                span.font-size-12 {{ categoryTop.name }}

</template>

<script>
import router from "@/router";
import {getData, urlPath} from '@/utils'

const HeaderBar = {
  data() {
    return {
      isShowCategoryInMobile: false,
      categoriesTop: []
    }
  },
  methods: {
    onShowCategory() {
      this.isShowCategoryInMobile = !this.isShowCategoryInMobile
    },
    gotoProductsPage(catName) {
      if (catName === this.categoriesTop[0]) router.push({name: urlPath.Home.name})
      else router.push({
        name: urlPath.Products.name,
        params: {categoryName: catName.name}
      }).catch((e) => {
        return
      })
    },
    async getCategory () {
      this.categoriesTop = this.$store.state.categories.categories
      if (this.categoriesTop.length === 0) {
        const data = await getData(['category'])
        this.$store.commit('updateCategories', data.categories)
      }
      this.categoriesTop = [{name: 'Trang chủ', id: 0}].concat(this.$store.state.categories.categories.filter(cate => cate.logo.url === null))
    }
  },
  mounted() {
    this.getCategory()
  }
}

export default HeaderBar
</script>

<style scoped lang="sass">
.header-color
  background-color: #f57e2e
.max-width
  max-width: 1200px
.center
  margin: 0 auto
  text-align: center
ul
  padding: 0
  justify-content: center
ul li
  text-align: center
  list-style: none
  margin: 0 3px
ul li:hover
  background-color: #faabcd
  cursor: pointer
.pc ul li
  display: inline-block
.category
  height: 40px
.font-size-12
  font-size: 13px
</style>