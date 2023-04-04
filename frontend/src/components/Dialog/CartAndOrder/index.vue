<template lang="pug">
  dialog-container(
    label="Giỏ hàng"
    @on-close="$emit('on-close')"
    :value="show"
    :width="1000"
  )
    span.title Giỏ Hàng
    v-data-table(
      :headers="headers"
      :items="carts"
      class="elevation-1"
    )
      template(v-slot:item.name="{item}")
        span {{item.product.name}}
      template(v-slot:item.image="{item}")
        v-img(:src="item.product.images[0].url" max-width="80" )
      template(v-slot:item.price="{item}")
        span {{item.product.price}}
      template(v-slot:item.action="{item}")
        v-chip.pointer(color="green" dark @click="onClickOrder(item)")
          span Đăt hàng
        v-chip.pointer(color="red" dark @click="deleteCart(item)")
          span Xóa

    span.title Đơn Mua
    v-data-table(
      :headers="headers"
      :items="orders"
      class="elevation-1"
    )
      template(v-slot:item.name="{item}")
        span {{item.product.name}}
      template(v-slot:item.image="{item}")
        v-img(:src="item.product.images[0].url" max-width="80" )
      template(v-slot:item.price="{item}")
        span {{item.product.price}}
      template(v-slot:item.action="{item}")
        v-chip.pointer(color="red" dark @click="deleteOrder(item)")
          span Xóa
    template(v-slot:actions)
      v-card-actions
</template>

<script>
import {defineComponent} from 'vue'
import DialogContainer from '../../DialogContainer/index.vue'
import {createData, deleteData} from "@/utils";

const CartAndOrderDialog = defineComponent({
    components: {DialogContainer},
    props: {
        show: {default: false},
        carts: {default: () => []},
        orders: {default: () => []}
    },
    setup(props, {emit}) {
        const user = JSON.parse(localStorage.getItem('user'))
        const headers = [
            {text: 'Hình ảnh', value: 'image', align: 'start',},
            {text: 'Tên sản phẩm', value: 'name'},
            {text: 'Giá', value: 'price'},
            {text: 'Số Lượng', value: 'quantity'},
            {text: '', value: 'action'}
        ]

        const onClickOrder = async (info) => {
            const body = {
                user: user.id,
                product: info.product.id,
                quantity: info.quantity,
                status: "confirm"
            }
            await createData('/order/', body)
            emit('update-cart-order')
        }

        const deleteCart = async (cart) => {
            await deleteData('/cart/', cart.id)
            emit('update-cart-order')
        }

        const deleteOrder = async (order) => {
            await deleteData('/order/', order.id)
            emit('update-cart-order')
        }

        return {
            headers,
            onClickOrder,
            deleteCart,
            deleteOrder
        }
    }
})

export default CartAndOrderDialog
</script>

<style lang="sass">
.pointer
  cursor: pointer
.title
  font-size: 17px
  color: green
  padding: 2px
</style>