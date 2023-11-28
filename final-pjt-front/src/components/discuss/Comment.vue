<template>
  <div>
    <div class="d-flex mb-3 align-items-center">
      <Icon icon="bxs:user" class="user-icon"/>
      <div>
        <div class="bg-light rounded-3 px-3 py-1">
          <strong>{{ comment.userName }}</strong>
          <small>{{ comment.content }}</small>
          <button @click="deleteComment" class="ml-10">
            <Icon icon="bx:x" />
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import { Icon } from '@iconify/vue2'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Comment',
  components: {
    Icon,
  },
  props: {
    comment: Object
  },
  methods: {
    async deleteComment() {
      await axios.delete(`${API_URL}/communities/${this.comment.community}/comments/${this.comment.id}/`)
      location.reload()
    },

  }
}
</script>

<style>
strong {
  margin-right: 10px;
}
</style>