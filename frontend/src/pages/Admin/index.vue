<template lang="pug">
    div.max-width
        h1.center.main-color Danh Muc
        v-data-table(
            :headers="HeaderCategory"
            :items="categories"
            class="elevation-1"
        )
            template(v-slot:header.actions)
                v-btn(@click="openDialog('category')")
                    span.main-color Them Danh Muc
            template(v-slot:item.actions='{ item }')
                v-icon.mr-2(small='' @click="openDialog('category', item)") mdi-pencil
                v-icon(small='') mdi-delete

        h1.center.main-color San Pham
        v-data-table(
            :headers="HeaderProducts"
            :items="products"
            class="elevation-1"
        )
            template(v-slot:header.actions)
                v-btn(@click="openDialog('product')")
                    span.main-color Them San Pham
            template(v-slot:item.category="{item}")
                span {{item.category.name}}
            template(v-slot:item.actions='{ item }')
                v-icon.mr-2(small='' @click="openDialog('product', item)")
                    | mdi-pencil
                v-icon(small='')
                    | mdi-delete

        h1.center.main-color Đơn Hàng
        v-data-table(
            :headers="HeaderOrder" class="elevation-1" :items="orders"
        )
            template(v-slot:item.name="{item}")
                span {{item.product.name}}
            template(v-slot:item.image="{item}")
                v-img(:src="item.product.images[0].url" max-width="80" )
            template(v-slot:item.price="{item}")
                span {{item.product.price}}
            template(v-slot:item.user="{item}")
                span {{item.user.name}}
            template(v-slot:item.tel="{item}")
                span {{item.user.tel}}
            template(v-slot:item.email="{item}")
                span {{item.user.email}}

        h1.center.main-color Giỏ Hàng
        v-data-table(
            :headers="HeaderOrder" class="elevation-1" :items="carts"
        )
            template(v-slot:item.name="{item}")
                span {{item.product.name}}
            template(v-slot:item.image="{item}")
                v-img(:src="item.product.images[0].url" max-width="80" )
            template(v-slot:item.price="{item}")
                span {{item.product.price}}
            template(v-slot:item.user="{item}")
                span {{item.user.name}}
            template(v-slot:item.tel="{item}")
                span {{item.user.tel}}
            template(v-slot:item.email="{item}")
                span {{item.user.email}}

        category-dialog(
            ref="category_dialog"
            :show="show.category"
            :item-data="itemData.category"
            :label="itemData.category ? 'Add' : 'Edit'"
            :is-add="isAdd.category"
            @on-close="show.category = false"
            @reload="reload"
        )

        product-dialog(
            ref="product_dialog"
            :categories="categories"
            :show="show.product"
            :item-data="itemData.product"
            :label="itemData.product ? 'Add' : 'Edit'"
            :is-add="isAdd.product"
            @on-close="show.product = false"
            @reload="reload"
        )

</template>

<script>
import {defineComponent, onMounted, ref, getCurrentInstance} from 'vue'
import {CategoryDialog, ProductDialog} from '@/components/Dialog'
import {HeaderCategory, HeaderProducts, HeaderCart, HeaderOrder} from './index.js'
import {getData} from "@/utils";

const Admin = defineComponent({
    components: {CategoryDialog, ProductDialog},
    setup() {
        const instance = getCurrentInstance().proxy
        const categories = ref([])
        const products = ref([])
        const carts = ref([])
        const orders = ref([])
        const show = ref({category: false, product: false})
        const itemData = ref({category: {}, product: {}})
        const isAdd = ref({category: false, product: false})

        const openDialog = (type, curItem = null) => {
            itemData.value[type] = curItem
            isAdd.value[type] = !curItem
            show.value[type] = true
        }

        const init = async () => {
            const data = await getData(['category', 'product', 'order', 'cart'])
            categories.value = data.categories
            products.value = data.products
            carts.value = data.cart
            orders.value = data.order
        }

        const reload = async () => {
            init()
        }

        onMounted(init)
        return {
            HeaderOrder,
            HeaderCart,
            HeaderCategory,
            categories,
            products,
            HeaderProducts,
            openDialog,
            show,
            itemData,
            isAdd,
            reload,
            carts,
            orders
        }
    }
})

export default Admin
</script>

<style lang="sass">
.center
  text-align: center

.main-color
  color: #f57e2e

.max-width
  max-width: 1000px
  margin: 0 auto
</style>