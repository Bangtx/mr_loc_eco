<template lang="pug">
  div
    header-bar
    .max-width.center
      v-row.pt-10.hidden-sm-and-down
        v-col(cols="2")
          categories(:items="outstandCategory" title="Nổi bật")
        v-col(cols="8")
          carousel
          h1.color-main.pt-5 Danh Sách Sản Phẩm
        v-col(cols="2")
          v-img(src="https://vn-test-11.slatic.net/p/1f519ee915f52566bcc8242bb797afe0.png")
      carousel.mt-3.hidden-md-and-up

      // category for mobile
      mobile-categories.hidden-md-and-up(:items="outstandCategory" title="Nổi bật")

      h1.color-main.hidden-md-and-up Danh Sách Sản Phẩm
      // pc
      v-row.hidden-sm-and-down
        v-col(cols="2")
          categories(title="Danh mục" :items="categories")
        v-col(cols="10")
          .list-product
            sub-product.pa-2(v-for="prd in products" :product="prd")
      // mobile
      v-row.hidden-md-and-up.hidden-sm-only
        v-col(cols="6" v-for="prd in products")
          v-list-item.pa-0
            sub-product(:product="prd")
      // tab
      v-row.hidden-md-and-up.hidden-xs-only
        v-col(cols="4" v-for="prd in products")
          v-list-item
            sub-product(:product="prd")
</template>

<script>
import {HeaderBar, Carousel, Categories, SubProduct, MobileCategories} from "@/components";
import {getData} from "@/utils";
import router from "@/router";

const Products = {
  components: {
    HeaderBar,
    Carousel,
    Categories,
    SubProduct,
    MobileCategories
  },
  data() {
    return {
      outstandCategory: [
        { text: 'Giá Tốt Mỗi Ngày', logo: {url: 'https://salt.tikicdn.com/cache/100x100/ts/upload/3c/ce/96/db8c083610e45b78d8f7662f0013faa8.png.webp' }},
        { text: 'Mã Giảm Giá', logo: {url: 'https://salt.tikicdn.com/cache/100x100/ts/upload/20/68/cf/6d4adbdbcd1c35b0a438a655d9a420d0.png.webp' }},
        { text: 'Ưu Đãi', logo: {url: 'https://salt.tikicdn.com/cache/100x100/ts/upload/4d/a3/cb/c86b6e4f17138195c026437458029d67.png.webp' }},
        { text: 'Giao Hàng', logo: {url: 'https://salt.tikicdn.com/cache/100x100/ts/tmp/6f/4e/41/93f72f323d5b42207ab851dfa39d44fb.png.webp' }},
        { text: 'Siêu Hot', logo: {url: 'https://salt.tikicdn.com/cache/100x100/ts/upload/6f/d0/68/76b6c01998c3f45f70b843c390097690.png.webp' }},
        { text: 'Mua Trước Trả Sau', logo: {url: 'https://salt.tikicdn.com/cache/100x100/ts/upload/44/58/fc/804a2dfd610e9075ad5a8f0d13f2b21a.png.webp' }},
      ],
      categories: [],
      products: [],
      categoryId: null,
      allCat: []
    }
  },
  methods: {
    async getProducts() {
      const data = await getData(['product'], {product: {category: this.categoryId}})
      this.products = data.products
    },
    async getCategories() {
      this.allCat = this.$store.state.categories.categories
      this.allCat = this.allCat.length === 0 ? (await getData(['category'])).categories : this.allCat
      this.$store.commit('updateCategories', this.allCat)

      // filter category on header
      this.categories = this.allCat.filter(cate => cate.logo !== null).map(cate => {
        return {...cate, icon: cate.logo, text: cate.name}
      })
    }
  },
  watch: {
    '$route.params.categoryName': {
      handler: async function(categoryName) {
        await this.getCategories()
        this.categoryId = this.allCat.find(cat => cat.name === categoryName).id
        await this.getProducts()
      },
      deep: true,
      immediate: true
    }
  }
}

export default Products
</script>

<style scoped lang="sass">
.max-width
  max-width: 1200px
.center
  margin: 0 auto
  text-align: center
.color-main
  color: #f57e2e
</style>