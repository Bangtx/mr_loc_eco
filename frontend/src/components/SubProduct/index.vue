<template lang="pug">
  .content.max-width-product-component.float-left(@click="onClick()")
    v-img.max-width-product-component(:src="product.images[0].url")
    .product-name.align-left
      span {{ product.name }}
    .product-review.align-left
      span {{ product.star }}
      v-icon(color="#f57e2e" ) mdi-star
      span | Đã bán: {{ product.sales }}
    .price.align-left
      h4 {{ product.price }} ₫
    .cmt.align-left {{ product.cmt }}
    v-divider
    .cmt.align-left {{ product.shipCmt }}
</template>

<script>
import router from '@/router'
import {urlPath} from '@/utils'

const SubProduct = {
  props: ['product'],
  methods: {
    onClick() {
      router.push({
        name: urlPath.ProductDetail.name,
        query: {
          product_id: this.product.id
        }
      })
    }
  }
}

export default SubProduct
</script>

<style scoped lang="sass">
.max-width-product-component
  max-width: 160px
  //height: 300px
  //background-color: #f57e2e
//@media only screen and (max-width 500px)
//  .max-width-product-compoment
//    max-width: 45%
//@media only screen and (max-width 1000px)
//  .max-width-product-compoment
//    max-width: 33%
.align-left
  text-align: left
.price
  font-size: 20px
.cmt
  font-size: 12px
  color: gray
.float-left
  float: left
.product-name
  height: 5em
  overflow: hidden
  //text-overflow: ellipsis
  //white-space: nowrap
  //word-wrap: break-word
.content:hover
  //display: block
  border: 2px solid #f57e2e
  transform: scale(1.05)
</style>