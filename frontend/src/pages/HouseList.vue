<template>
  <div>
  <q-card class="q-mx-auto q-my-lg" style="width: 80%">
    <q-card-section>
      <p class="text-h2 q-mt-lg">House list</p>
    </q-card-section>
    <q-card-section>
      <q-table
        :data="houses"
        :columns="columns"
        :pagination.sync="pagination"
        row-key="id"
        :loading="loading"
      >
        <template v-slot:top>
          <q-btn v-if="isAdmin" color="primary" :disable="loading" label="Add house" @click="addDialog = true" />
          <q-btn v-if="isAdmin" class="q-ml-sm" color="primary" :disable="loading" label="Remove house" @click="deleteDialog = true" />
        </template>
        <template v-slot:body-cell-actions="props">
          <q-td :props="props">
            <q-btn dense round flat color="primary" @click="onClick(props)" icon="info"></q-btn>
          </q-td>
        </template>
      </q-table>
    </q-card-section>
  </q-card>
  <q-dialog v-model="addDialog" class="bg-white" persistent style="width: 400px;">
    <q-card class="q-pa-xl">
      <q-form
        @submit="onSubmit"
        style="width: 400px"
      >
        <q-input
          filled
          v-model="new_house_toward"
          label="House toward *"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please type a house toward']"
        />

        <q-input
          filled
          type="number"
          v-model="new_house_unit_price"
          label="House unit price *"
          lazy-rules
          :rules="[
              val => val !== null && val !== '' || 'Please type house unit price',
              val => val > 0 || 'Please type a positive unit price'
            ]"
        />

        <q-input
          filled
          type="number"
          v-model="new_building_area"
          label="House building area *"
          lazy-rules
          :rules="[
              val => val !== null && val !== '' || 'Please type house building area',
              val => val > 0 || 'Please type a positive building area'
            ]"
        />

        <q-input
          filled
          type="number"
          v-model="new_total_price"
          label="House total price *"
          lazy-rules
          :rules="[
              val => val !== null && val !== '' || 'Please type house total price',
              val => val > 0 || 'Please type a positive total price'
            ]"
        />

        <q-input
          filled
          v-model="new_decoration"
          label="House decoration *"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please type a house decoration']"
        />

        <q-input
          filled
          v-model="new_floors"
          label="House floor *"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please a house floor']"
        />

        <q-input
          filled
          v-model="new_unit_type"
          label="House unit type *"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please a house unit type']"
        />

        <q-select v-model="new_intermediary_name" :options="options" label="Standard" />

        <q-input
          filled
          v-model="new_area"
          label="House area *"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please a house area']"
        />

        <q-input
          filled
          v-model="new_community_name"
          label="House community name *"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please a house community name']"
        />

        <q-input
          filled
          v-model="new_part_area"
          label="House part area *"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please a house part area']"
        />

        <div>
          <q-btn label="Submit" type="submit" color="primary"/>
          <q-btn label="Cancel" color="primary" flat class="q-ml-sm" v-close-popup />
        </div>
      </q-form>
    </q-card>
  </q-dialog>
    <q-dialog v-model="deleteDialog" class="bg-white" persistent style="width: 400px;">
      <q-card class="q-pa-xl">
        <q-form
          @submit="onDelete"
          style="width: 400px"
        >
          <q-input
            filled
            v-model="delete_id"
            label="House id to delete *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please type a house id to delete']"
          />
          <div>
            <q-btn label="Remove" type="submit" color="primary"/>
            <q-btn label="Cancel" color="primary" flat class="q-ml-sm" v-close-popup />
          </div>
        </q-form>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
export default {
  name: "HouseList",
  data () {
    return {
      loggedIn: false,
      isAdmin: false,
      houses: [],
      filter: '',
      loading: true,
      addDialog: false,
      deleteDialog: false,
      delete_id: '',
      new_house_toward: '',
      new_house_unit_price: 0,
      new_building_area: 0,
      new_total_price: 0,
      new_decoration: '',
      new_floors: '',
      new_unit_type: '',
      new_intermediary_name: '华发地产',
      new_phone: 0,
      new_area: '',
      new_community_name: '',
      new_part_area: '',
      options: [
        '华发地产',
        'Q房地产',
        '品房阁',
        '正顺地产'
      ],
      columns: [
        {
          name: 'ID',
          required: true,
          label: 'House ID',
          align: 'left',
          field: row => row.house_id,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: 'Toward',
          required: true,
          label: 'House Toward',
          align: 'left',
          field: row => row.toward,
          sortable: true
        },
        {
          name: 'Unit price',
          required: true,
          label: 'Unit price',
          align: 'left',
          field: row => row.unit_price,
          format: val => `¥${val}`,
          sortable: true
        },
        {
          name: 'Building area',
          required: true,
          label: 'Building area',
          align: 'left',
          field: row => row.building_area,
          format: val => `${val}m²`,
          sortable: true
        },
        {
          name: 'Total price',
          required: true,
          label: 'Total price',
          align: 'left',
          field: row => row.total_price,
          format: val => `¥${val}W`,
          sortable: true
        },
        {
          name: 'Decoration',
          required: true,
          label: 'Decoration',
          align: 'left',
          field: row => row.decoration,
          sortable: true
        },
        {
          name: 'Floor',
          required: true,
          label: 'Floor',
          align: 'left',
          field: row => row.floors,
          sortable: true
        },
        {
          name: 'Unit type',
          required: true,
          label: 'Unit type',
          align: 'left',
          field: row => row.unit_type,
          sortable: true
        },
        { name: 'actions', label: 'Actions', field: '', align:'center' }
      ],
      pagination: {
        rowsPerPage: 10
      }
    }
  },
  created() {
    this.loggedIn = sessionStorage.getItem('loggedIn') !== null
    if(this.loggedIn) {
      if(this.$route.path === '/' || this.$route.path === '/reg')
        this.$router.push('/index')
    }
    else {
      if(this.$route.path !== '/' && this.$route.path !== '/reg')
        this.$router.push('/')
    }
    this.username = sessionStorage.getItem('loggedIn')
    this.isAdmin = sessionStorage.getItem('role') === '1'
    let _this = this
    this.loading = true
    this.$axios.get('http://127.0.0.1:8000/api/get_list').then(function (response) {
      let res = response.data
      for(let i = 0; i < res.length; i++) {
        _this.houses.push(res[i])
      }
      _this.$forceUpdate()
    })
    this.loading = false
  },
  methods: {
    onSubmit() {
      let _this = this
      switch(this.new_intermediary_name) {
        case "华发地产":
          this.new_phone = 7568678828
          break
        case "Q房地产":
          this.new_phone = 7567230898
          break
        case "品房阁":
          this.new_phone = 89888261596
          break
        case "正顺地产":
          this.new_phone = 4001680808
          break;
      }
      this.$axios.post('http://127.0.0.1:8000/api/create', {
        uid: sessionStorage.getItem('user_id'),
        toward: _this.new_house_toward,
        unit_price: _this.new_house_unit_price,
        building_area: _this.new_building_area,
        total_price: _this.new_total_price,
        decoration: _this.new_decoration,
        floors: _this.new_floors,
        unit_type: _this.new_unit_type,
        intermediary_name: _this.new_intermediary_name,
        phone: _this.new_phone,
        area: _this.new_area,
        community_name: _this.new_community_name,
        part_area: _this.new_part_area
      }).then(function (response) {
        console.log(response)
        let res = response.data
        if(res.status === 'Success') {
          _this.$q.notify({
            type: 'positive',
            message: 'Successfully added.'
          })
          _this.addDialog = false
        } else {
          _this.$q.notify({
            type: 'negative',
            message: 'Add error.'
          })
        }
      }).catch(function (error) {
        console.log(error)
        _this.$q.notify({
          type: 'negative',
          message: 'Internal error.'
        })
      })
    },
    onDelete() {
      let _this = this
      this.$axios.post('http://127.0.0.1:8000/api/delete', {
        uid: sessionStorage.getItem('user_id'),
        house_id: _this.delete_id
      }).then(function (response) {
        console.log(response)
        let res = response.data
        if(res.status === 'Success') {
          _this.$q.notify({
            type: 'positive',
            message: 'Successfully removed.'
          })
          _this.deleteDialog = false
        } else {
          _this.$q.notify({
            type: 'negative',
            message: 'Remove error.'
          })
        }
      }).catch(function (error) {
        console.log(error)
        _this.$q.notify({
          type: 'negative',
          message: 'Internal error.'
        })
      })
    },
    onClick(props) {
      console.log(props)
      this.$router.push({
        name: 'info',
        params: {
          id: props.row.house_id
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
