<template lang="pug" xmlns="">
  div
    header-bar(ref="headerBar")
    .max-width.center
      product-detail.max-width.center.pt-10
      v-divider.mt-5
      h1.color-main.text-center Sản Phẩm Tương Tự
      .list-product
        v-btn.mt-10(icon @click="onScrollX('prev')")
          v-icon(x-large) mdi-skip-previous-circle-outline
        .list-product-content(ref="listProduct" )
          sub-product.pa-2(v-for="prd in newestProducts" :product="prd")
        v-btn.mt-10(icon @click="onScrollX('next')")
          v-icon(x-large) mdi-skip-next-circle-outline
    footer-bar
</template>

<script>
import {HeaderBar, ProductDetail, SubProduct, FooterBar} from '@/components'
import {getData} from "@/utils";

const Detail = {
  components: {
    HeaderBar,
    ProductDetail,
    SubProduct,
    FooterBar
  },
  data() {
    return {
      newestProducts: []
    }
  },
  provide() {
    return {
      'detailPage': this
    }
  },
  methods: {
    async getNewestProducts() {
      this.newestProducts = (await getData(['product'], {product: {limit: 6}})).products
    },
    onScrollX(action) {
      let pos = this.$refs.listProduct.scrollLeft
      if (pos < 0) return
      if (action === 'prev') pos -= 300
      if (action === 'next') pos += 300
      this.$refs.listProduct.scroll({left: pos, behavior: 'smooth'})
    }
  },
  watch: {
    '$route.query.product_id': {
      handler: async function() {
        await this.getNewestProducts()
      },
      deep: true,
      immediate: true
    }
  }
}

export default Detail
</script>

<style scoped lang="sass">
.center
  margin: 0 auto
  text-align: center
.max-width
  max-width: 1200px
.center
  margin: 0 auto
  text-align: center
.color-main
  color: #f57e2e
.list-product
  display: flex
  box-sizing: border-box
.list-product-content
  width: 90%
  margin: 0 auto
  display: flex
  overflow-x: auto
  box-sizing: border-box
.list-product-content::-webkit-scrollbar
  width: 0
</style>