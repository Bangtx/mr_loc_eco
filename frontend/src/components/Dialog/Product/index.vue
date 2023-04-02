<template lang="pug">
    dialog-container(
        :label="label"
        :mode="isAdd ? 'create' : 'update'"
        :loading="loading"
        @on-close="closeDialog"
        @on-update="updateItem"
        @on-create="createItem"
        @on-typing="onTyping"
        v-model="show"
        :width="800"
        height="90vh"
    )
        v-row.pt-1
            v-col.pa-1.px-1
                image-list(
                    :images="masterData.images"
                    @on-change="(input) => {pictures = input}"
                    @on-remove="removeImage"
                )
        v-row
            v-col.pa-1(cols="12" sm="6")
                v-autocomplete(
                    hide-details label="Danh mục"
                    :items="categories" item-text="name" item-value="id" v-model="masterData.category"
                )
            v-col.pa-1(cols="12" sm="6")
                v-text-field#name(
                    ref="name" label="Tên sản phẩm"
                    hide-details
                    v-model="masterData.name"
                    @focus="onClickInput('name')"
                )
            v-col.pa-1(cols="12" sm="6")
                v-text-field#cost(
                    ref="cost" label="Giá gốc"
                    hide-details
                    v-model="masterData.cost"
                    @focus="onClickInput('cost')"
                )
            v-col.pa-1(cols="12" sm="6")
                v-text-field#price(
                    ref="price" label="Giá sau khi giảm"
                    hide-details
                    v-model="masterData.price"
                    @focus="onClickInput('price')"
                )
            v-col.pa-1(cols="12" sm="6")
                v-text-field#star(
                    ref="price" label="Đánh giá (sao)"
                    hide-details
                    v-model="masterData.star"
                    @focus="onClickInput('star')"
                )
            v-col.pa-1(cols="12" sm="6")
                v-text-field#sales(
                    ref="sales" label="Đã bán"
                    hide-details
                    v-model="masterData.sales"
                    @focus="onClickInput('sales')"
                )
            v-col.pa-1(cols="12" sm="6")
                v-text-field#comment(
                    ref="comment" label="Chú thích"
                    hide-details
                    v-model="masterData.comment"
                    @focus="onClickInput('comment')"
                )
            v-col.pa-1(cols="12" sm="6")
                v-text-field#ship_comment(
                    ref="ship_comment" label="Chú thích về ship"
                    hide-details
                    v-model="masterData.ship_comment"
                    @focus="onClickInput('ship_comment')"
                )
        v-row
          h3.pl-1 Mô tả sản phẩm
          vue-editor.pt-3(v-model="masterData.description")

</template>
<script>
import {defineComponent, getCurrentInstance, toRefs, watch, ref} from 'vue'
import DialogContainer from '../../DialogContainer/index.vue'
import ImageList from "@/components/ImageList/index.vue";
import {createData, updateData, deleteData} from "@/utils";
import { VueEditor } from "vue2-editor";
// import { api } from '@/plugins'
// import { endpoints, showError } from '@/utils'

const ProductDialog = defineComponent({
    components: {
        DialogContainer, ImageList, VueEditor
    },
    props: {
        show: {
            type: Boolean,
            required: true
        },
        itemData: {
            type: Object,
            default: null
        },
        loading: {
            type: Boolean,
            default: false
        },
        label: {
            type: String,
            default: ''
        },
        isAdd: {
            default: true
        },
        categories: {
            default: () => []
        }
    },
    setup(props, {emit}) {
        const {itemData, show} = toRefs(props)
        const masterData = ref({})
        const instance = getCurrentInstance()
        const {$refs, $toast, $root} = instance.proxy
        const isCompositingInput = ref(true)
        const isClearGroup = ref(false)
        const STATE_LIST = ['name']
        const focusInput = ref(STATE_LIST[0])
        const enterKeydown = ref(0)
        const pictures = ref([])

        const onClickInput = (refName) => {
            isClearGroup.value = false
            emit('on-click-input', refName)
        }

        const closeDialog = () => {
            emit('on-close')
        }

        const convertData = () => {
            Object.keys(masterData.value).forEach((key) => {
                if (masterData.value[key] === '') masterData.value[key] = null
            })
        }

        const removeImage = async (image) => {
            await deleteData('/image/', image)
        }

        const generateBody = () => {
            return {
                ...masterData.value,
                images: [... new Set((masterData.value.images || []).concat(pictures.value))]
            }
        }

        const createItem = async () => {
            convertData()
            const body = generateBody()
            await createData('/product/', body)
            emit('on-close')
            emit('reload')
            // emit('on-create', masterData.value)
        }

        const updateItem = async () => {
            convertData()
            const body = generateBody()
            await updateData('/product/', body.id, body)
            emit('on-close')
            emit('reload')
        }

        const onKeyDown = (event) => {
            isCompositingInput.value = event.key === 'Enter'
        }

        const onTyping = (event) => {
            if (isCompositingInput.value) emit('on-typing', event)
        }

        const init = async () => {
            focusInput.value = STATE_LIST[0]
            enterKeydown.value = 0
            if (props.show) {
                const initProduct = {
                    category: null, name: null, cost: null, price: null, star: null, images: [],
                    description: null, sales: null, comment: null, ship_comment: null
                }
                masterData.value = props.isAdd
                    ? JSON.parse(JSON.stringify(initProduct))
                    : JSON.parse(JSON.stringify({...itemData.value, category: itemData.value.category.id}))
                // console.log(props.isAdd, masterData.value)
            }
        }

        watch(
            () => show.value,
            () => {
                if (show.value) init()
            }
        )

        watch(
            () => itemData.value,
            () => {
                STATE_LIST.forEach((element) => {
                    document.getElementById(element)?.addEventListener('keydown', onKeyDown)
                })
            }
            , {
                deep: true
            }
        )

        return {
            closeDialog,
            updateItem,
            createItem,
            onClickInput,
            isCompositingInput,
            onTyping,
            masterData,
            pictures,
            removeImage
        }
    }
})

export default ProductDialog
</script>

<style lang="sass" scoped>
.container
  display: grid
  grid-gap: 15px
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))
  padding-right: 0
  padding-left: 0

.container > div
  object-fit: cover
  border: 1px solid #3c3c3c

  .title-children
    background-color: #008037
    color: white
    padding: 10px
    text-align: center

  .content
    padding: 10px

.required
  content: '99'
  color: red
</style>