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
        products: null
    }
    const queryProduct = query?.product ? objectToString(query.product) : ''

    try {
        await Promise.all([
            listData.includes('category') ? api.get('/category/').then(({data}) => result.categories = data) : null,
            listData.includes('product') ? api.get(`/product?${queryProduct}`).then(({data}) => result.products = data) : null
        ])
    } catch (e) {
        console.log(e)
    }

    return result
}


export const createData = async (endpoint, data) => {
    try {
        await api.post(endpoint, data)
        Vue.$toast.success('create successful')
    } catch (e) {
        console.log(e)
    }
}


export const updateData = async (endpoint, id, data) => {
    try {
        await api.put(`${endpoint}${id}`, data)
        Vue.$toast.success('update successful')
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