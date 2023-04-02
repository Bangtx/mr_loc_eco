<template lang="pug">
  div
    v-row
      v-col(:cols="screenType === 'pc' ? 4 : (screenType === 'tab' ? 5 : 12)")
        .pa-4
          v-row
            v-col(cols="12")
              v-img(:src="product.images[0].url")
          v-row
            v-col(cols="3" v-for="img in product.images" :key="img.url")
              v-img(:src="img.url")
            //v-col(cols="3")
            //  v-img(src="https://salt.tikicdn.com/cache/100x100/ts/product/89/3e/19/ad4dab5a03110603cba836c3853b2ae1.jpg.webp")
            //v-col(cols="3")
            //  v-img(src="https://salt.tikicdn.com/cache/100x100/media/catalog/producttmp/27/ce/66/efc719247e9dfe784acee4004e80f9ed.jpg.webp")
            //v-col(cols="3")
            //  v-img(src="https://salt.tikicdn.com/cache/100x100/ts/product/31/eb/8d/2ae1397fa0ee2365f86a7e9df1dce005.jpg.webp")
      v-col(:cols="screenType === 'pc' ? 8 : (screenType === 'tab' ? 7 : 12)")
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

const ProductDetail = {
  props: ['screenType', 'product'],
  components: {
    FastInputQuantity
  },
  methods: {
    changeQuantity(action) {
      if (this.product.quantity === 0 && action === '-') return
      if (action === '+') this.product.quantity += 1
      if (action === '-') this.product.quantity -= 1
    }
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