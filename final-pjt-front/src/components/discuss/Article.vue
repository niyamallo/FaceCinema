<template>
  <tbody id="board">
    <tr>
      <td scope="row" class="text-nowrap">
        {{ article.id }}
      </td>
      <td class="text-start">
        <router-link :to="{ name: 'Detail', params: { id: article.id }}" class="router-link">
          <strong>
            {{ article.title }}
          </strong>
        </router-link>
        <div class="my-2">
          <span>{{ article.userName }}</span>
          <span v-if="article.userName=='admin'" class="badge mx-1 bg-color">staff</span>
          <span v-else class="badge mx-1 pt-color">user</span>
        </div>
      </td>
      <td>
        <span>0</span>
        <span>💬</span>
      </td>
    </tr>
  </tbody>
</template>

<script>
export default {
  name: 'Article',
  props: {
    article: Object,
  },
}
</script>

<style scoped>
  .router-link {
    text-decoration: none;
    color: black;
  }
  .bg-color {
    background-color: #2A2B30;
  }
  .pt-color {
    background-color: #F7D54D;
  }
</style>