import api from "@/plugins/api"
import Vue from "vue";


const objectToString = (object) => {
    let result = ''
    Object.keys(object).forEach(key => {
        result += `${key}=${object[key]}`
    })
    return result
}


export const getData = async (listData = [], query = {}) => {
    const result = {
        categories: null,
        products: null,
        cart: null,
        order: null
    }
    const queryProduct = query?.product ? objectToString(query.product) : ''
    const queryCart = query?.cart ? objectToString(query.cart) : ''
    const queryOrder = query?.order ? objectToString(query.order) : ''

    try {
        await Promise.all([
            listData.includes('category') ? api.get('/category/').then(({data}) => result.categories = data) : null,
            listData.includes('product') ? api.get(`/product/?${queryProduct}`).then(({data}) => result.products = data) : null,
            listData.includes('cart') ? api.get(`/cart/?${queryCart}`).then(({data}) => result.cart = data) : null,
            listData.includes('order') ? api.get(`/order/?${queryOrder}`).then(({data}) => result.order = data) : null
        ])
    } catch (e) {
        Vue.$toast.error('get data failed')
    }

    return result
}


export const createData = async (endpoint, payload, showMsg= true) => {
    try {
        const {data} = await api.post(endpoint, payload)
        if (showMsg) Vue.$toast.success('create successful')
        return data
    } catch (e) {
        this.$toast.error('create failed')
    }
    return null
}


export const updateData = async (endpoint, id, data) => {
    try {
        await api.put(`${endpoint}${id}`, data)
        Vue.$toast.success('update successful')
    } catch (e) {
        this.$toast.error('update failed')
    }
}


export const deleteData = async (endpoint, id) => {
    try {
        await api.delete(`${endpoint}${id}`)
        Vue.$toast.success('delete successful')
    } catch (e) {
        console.log(e)
    }
}


export const readFile = (file) => {
  return new Promise((resolve) => {
    const reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onloadend = () => resolve(reader.result)
  })
}