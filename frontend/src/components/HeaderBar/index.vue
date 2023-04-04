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
        v-menu(transition='slide-x-transition' bottom='' right='')
          template(v-slot:activator='{ on, attrs }')
            div(v-bind='attrs' v-on='on' @click="openAccountDialog")
              v-icon(color="white") mdi-account
              span.white--text.hidden-sm-and-down.font-size-12 {{user ? user.name : 'Tài Khoản '}}
          v-list(v-if="user !== null")
            v-list-item.cursor(@click="onLogout") Đăng xuất
        .ml-3
          v-btn(icon @click="openCartDialog")
            v-icon(color="white" ) mdi-cart-outline
            span.white--text.cart-quantity {{ carts.length }}
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

    account-dialog(
      ref="accountDialog"
      :show="isOpenAccountDialog"
      @on-close="isOpenAccountDialog = false"
      @update-cart-order="getCartAndOrder"
      @update-user="updateUser"
    )

    cart-and-order-dialog(
      :show="isOpenCartDialog"
      :carts="carts"
      :orders="orders"
      @update-cart-order="getCartAndOrder"
      @on-close="isOpenCartDialog = false"
    )
</template>

<script>
import router from "@/router";
import {getData, urlPath} from '@/utils'
import {AccountDialog, CartAndOrderDialog} from "@/components/Dialog";

const HeaderBar = {
  components: {AccountDialog, CartAndOrderDialog},
  data() {
    return {
      isShowCategoryInMobile: false,
      categoriesTop: [],
      isOpenAccountDialog: false,
      user: JSON.parse(localStorage.getItem('user')),
      carts: [],
      orders: [],
      isOpenCartDialog: false
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
      this.categoriesTop = [{name: 'Trang chủ', id: 0}].concat(this.$store.state.categories.categories)
    },
    async getCartAndOrder() {
      if (this.user) {
        const data = await getData(
          ['cart', 'order'], {cart: {user: this.user.id}, order: {user: this.user.id}}
        )
        this.carts = data.cart
        this.orders = data.order
      } else {
        this.carts = []
        this.orders = []
      }
    },
    openAccountDialog() {
      if (this.user) return
      this.isOpenAccountDialog = true
    },
    openCartDialog() {
      if (this.carts.length === 0) {
        this.$toast.error('Giỏ hàng trống')
        return
      }
      this.isOpenCartDialog = true
    },
    updateUser() {
      this.user = JSON.parse(localStorage.getItem('user'))
    },
    onLogout() {
      this.user = null
      this.carts = []
      localStorage.removeItem('user')
    }
  },
  mounted() {
    this.getCategory()
    this.getCartAndOrder()
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
.cursor
  cursor: pointer
</style>