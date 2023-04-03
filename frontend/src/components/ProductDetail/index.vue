<template lang="pug">
  div
    v-row
      //v-col(:cols="screenType === 'pc' ? 4 : (screenType === 'tab' ? 5 : 12)")
      v-col(cols="12" sm="5" md="4")
        .pa-4
          v-row
            v-col(cols="12")
              v-img(:src="mainImage ? mainImage.url : product.images[0].url")
          v-row
            v-col(cols="3" v-for="img in product.images" :key="img.url" @click="mainImage = img")
              v-img(:src="img.url")
      v-col(cols="12" sm="7" md="8")
        .pa-4
          p.align-left Thương hiệu: {{ product.trademark }}
          h1.align-left {{ product.name }}
          p.align-left
            v-icon(v-for="i in product.star" color="#f57e2e") mdi-star
            span.pa-6 Đã bán: {{ product.sales }}
          p.align-left
            del {{ product.cost }} ₫ -->
            span.price {{ product.price }} ₫
          p.align-left
            span Vận Chuyển
            v-icon.pl-3(color="#f57e2e") mdi-plane-car
            span.pl-3 Miễn phí vận chuyển
          p.align-left Vân chuyển từ Hà Nội
          div.discount
            p.pl-2.title-discount.align-left Mua Số Lượng Lớn Để Nhận Ưu Đãi
            v-checkbox.pl-2(
              label="Mua 10 sản phẩm để giảm giá"
            )
          p.align-left.pt-4 Số Lượng
          fast-input-quantity.align-left(
            :value="product.quantity || 0"
            @change-value="changeQuantity"
          )
          // cancel float left
          div(style="clear:both;")
          v-list-item.pa-0
            v-btn(color="#f57e2e" :disabled="product.quantity === 0").white--text.align-left.mt-2 Mua Hàng Ngay
            v-btn.align-left.mt-2.ml-2(:disabled="product.quantity === 0")
              span.main-color Thêm Vào Giỏ Hàng
      v-col(cols="12")
        h3.main-color Mô Tả Sản Phẩm
        div.align-left.pa-2(v-html="product.description")

</template>

<script>
import FastInputQuantity from '../FastInputQuantity/index.vue'
import api from "../../plugins/api";
import router from "@/router";

const ProductDetail = {
  props: ['screenType'],
  components: {
    FastInputQuantity
  },
  data() {
    return {
      product: {images: [{url: null}]},
      mainImage: null
    }
  },
  mounted() {
    const {product_id} = router.currentRoute.query
    this.getProduct(product_id)
  },
  methods: {
    changeQuantity(action) {
      if (this.product.quantity === 0 && action === '-') return
      if (action === '+') this.product.quantity += 1
      if (action === '-') this.product.quantity -= 1
    },
    async getProduct(product_id) {
      try {
        const {data} = await api.get(`/product/get_one/${product_id}`)
        this.product = { ...data, quantity: 1 }
      } catch (e) {
        console.log(e)
      }
    },
  }
}

export default ProductDetail
</script>

<style scoped lang="sass">
.align-left
  text-align: left
.price
  color: rgb(255, 57, 69)
  font-size: 30px
.discount
  width: 350px
  border: 2px solid #f57e2e
  border-radius: 5px
.title-discount
  font-size: 18px
.main-color
  color: #f57e2e
</style>