<template lang="pug">
  div
    header-bar
    .max-width.center
      v-row.pt-10.hidden-sm-and-down
        v-col(cols="2")
          categories(:items="outstandCategory" title="Nổi bật")
        v-col(cols="8")
          carousel
          h1.color-main.pt-5 Chào Mừng Đến Với autoxuanphuc
        v-col(cols="2")
          v-img(src="https://vn-test-11.slatic.net/p/1f519ee915f52566bcc8242bb797afe0.png")
          h2.color-main Bọc vô lăng cao cấp
      carousel.mt-3.hidden-md-and-up
      // category for mobile
      //mobile-categories.hidden-md-and-up(:items="outstandCategory" title="Nổi bật")

      // cancel float left
      div(style="clear:both;")
      v-img.hidden-md-and-up(src="https://newsupdatetimes.com/wp-content/uploads/2021/01/Grand-Auto-Bazaar1-c3opy.jpg")
      h1.color-main.hidden-md-and-up Chào Mừng Đến Với autoxuanphuc

      // pc
      v-row.pt-2.hidden-sm-and-down
        v-col(cols="2")
          categories(title="Danh mục" :items="categories")
        v-col(cols="10")
          .trademark.linear-color.pl-1
            v-list-item.pa-0
              v-img.float-left.ma-2.justify-center(src="@/assets/toyota.png" width="110")
              v-img.float-left.ma-2.justify-center(src="@/assets/huyndai.png" width="110")
              v-img.float-left.ma-2.justify-center(src="@/assets/Kia.png" width="110")
              v-img.float-left.ma-2.justify-center(src="@/assets/mazda.png" width="110")
              v-img.float-left.ma-2.justify-center(src="@/assets/mec.png" width="110")
        //v-col(cols="10")
          v-carousel(hide-delimiters='' :hide-overflow='false' :per-page='5' :items-per-page='5' style='width: 500px;')
            v-carousel-item.carousel-item(v-for='(item, index) in items' :key='index')
              v-img.carousel-image(:src='item.src')

      // mobile
      .trademark.linear-color.hidden-md-and-up.pl-1
        v-list-item.pa-0
          v-img.float-left.ma-2.justify-center(src="@/assets/toyota.png" width="110")
          v-img.float-left.ma-2.justify-center(src="@/assets/huyndai.png" width="110")
          v-img.float-left.ma-2.justify-center(src="@/assets/Kia.png" width="110")
          v-img.float-left.ma-2.justify-center(src="@/assets/mazda.png" width="110")
          v-img.float-left.ma-2.justify-center(src="@/assets/mec.png" width="110")

      h2.color-main.mt-10 Danh sách sản phẩm nổi bật
      // pc
      v-row.hidden-sm-and-down
        v-col(cols="2")
        v-col(cols="10")
          .list-product
            sub-product.pa-2(v-for="prd in products" :product="prd")
      // mobile
      v-row.hidden-md-and-up.hidden-sm-only
        v-col(cols=6 v-for="prd in products" style="float: left")
          v-list-item.pa-0
            sub-product(:product="prd")
      //div(v-for="prd in products" style="float: left")
      //  v-list-item.pa-0
      //    sub-product(:product="prd")
      // tab
      v-row.hidden-md-and-up.hidden-xs-only
        v-col(cols="4" v-for="prd in products")
          v-list-item
            sub-product.pa-1(:product="prd")

</template>

<script>
import {HeaderBar, Categories, Carousel, SubProduct, MobileCategories} from '@/components'
import api from '@/plugins/api'
import {getData} from '@/utils'

const Home = {
  components: {
    HeaderBar,
    Categories,
    Carousel,
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
      products: []
    }
  },
  methods: {
    async getCategory () {
      this.categories = this.$store.state.categories.categories
      const listData = this.categories.length === 0 ? ['category', 'product'] : ['product']

      const data = await getData(listData)
      this.categories = this.categories.length === 0 ? data.categories : this.categories

      this.$store.commit('updateCategories', this.categories)
      this.categories = this.categories.filter(cate => cate.logo !== null).map(cate => {
        return {...cate, icon: cate.logo, text: cate.name}
      })
        console.log(this.categories )
      this.products = data.products
    }
  },
  mounted() {
    this.getCategory()
  }
}

export default Home
</script>

<style lang="sass" scoped>
.max-width
  max-width: 1200px
.center
  margin: 0 auto
  text-align: center
.color-main
  color: #f57e2e
.linear-color
  display: block
  overflow: auto
  background-image: linear-gradient(#fef0e6, white)
</style>