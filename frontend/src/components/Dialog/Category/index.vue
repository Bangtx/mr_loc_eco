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
        :width="400"
    )
        v-row.pt-1
            v-col.px-1
                image-list(
                    :images="masterData.logo"
                    @on-change="(input) => {pictures = input}"
                    @on-remove="removeImage"
                )
        v-text-field#name(
            ref="name"
            v-model="masterData.name"
            @focus="onClickInput('name')"
        )

</template>
<script>
import {defineComponent, getCurrentInstance, toRefs, watch, ref} from 'vue'
import DialogContainer from '../../DialogContainer/index.vue'
import ImageList from "@/components/ImageList/index.vue";
import {createData, updateData} from "@/utils";
// import { api } from '@/plugins'
// import { endpoints, showError } from '@/utils'

const CategoryDialog = defineComponent({
    components: {
        DialogContainer, ImageList
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

        const removeImage = (image) => {
            // const {url} = image
            // listImage.value = listImage.value.filter((i) => i.url !== url)
            // emit('on-change', listImage.value)
            // if (image.id) {
            //     emit('on-remove', image.id)
            // }
        }

        const generateBody = () => {
            return {
                ...masterData.value,
                logo: pictures.value.length > 0 ? pictures.value[0] : {payload: null, url: null, id: null}
            }
        }

        const createItem = async () => {
            convertData()
            const body = generateBody()
            await createData('/category/', body)
            emit('on-close')
            emit('reload')
            // emit('on-create', masterData.value)
        }

        const updateItem = async () => {
            convertData()
            const body = generateBody()
            await updateData('/category/', body.id, body)
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
                masterData.value = props.isAdd
                    ? JSON.parse(JSON.stringify({name: '', logo: []}))
                    : JSON.parse(JSON.stringify({...itemData.value, logo: [itemData.value.logo]}))
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

export default CategoryDialog
</script>

<style lang="sass" scoped>
.container
  display: grid
  grid-gap: 15px
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))
  padding-right: 0px
  padding-left: 0px

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