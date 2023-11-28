<template>
  <div>
    <section class="h-100 gradient-custom-2">
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col col-lg-9 col-xl-7">
            <div class="card">
              <div class="rounded-top text-white d-flex flex-row" style="background-color: #2A2B30; height:200px;">
                <div class="ms-4 mt-5 d-flex flex-column" style="width: 150px;">
                  <img src="https://i.namu.wiki/i/fxFCVlWGt54gGTsZ6HlWr5acHR0IOS08Cg9C-322MPEVbX5rvPjw4N2jhOtBVf5S7fCN_XO7JH8BuB7xj72yWw.webp"
                    alt="Generic placeholder image" class="img-fluid img-thumbnail mt-4 mb-2"
                    style="width: 150px; z-index: 1">
                  <button type="button" class="btn btn-outline-dark" data-mdb-ripple-color="dark"
                    style="z-index: 1;">
                    Edit profile
                  </button>
                </div>
                <div class="ms-3 text-start" style="margin-top: 130px;">
                  <h5>Salvador Dali</h5>
                  <p class="fst-italic">@itsMeDali</p>
                </div>
              </div>
              <div class="p-4 text-black" style="background-color: #f8f9fa;">
                <div class="d-flex justify-content-end text-center py-1">
                  <div>
                    <p class="mb-1 h5">123</p>
                    <p class="small text-muted mb-0">Movies</p>
                  </div>
                  <div class="px-3">
                    <p class="mb-1 h5">17</p>
                    <p class="small text-muted mb-0">Reviews</p>
                  </div>
                  <div>
                    <p class="mb-1 h5">5</p>
                    <p class="small text-muted mb-0">Articles</p>
                  </div>
                </div>
              </div>
              <div class="card-body p-4 text-black">
                <div class="mb-5">
                  <p class="lead fw-normal mb-1">About</p>
                  <div class="p-4" style="background-color: #f8f9fa;">
                    <p class="font-italic mb-1">Innovative artist</p>
                    <p class="font-italic mb-1">with surreal dream</p>
                    <p class="font-italic mb-0">from Spain.</p>
                  </div>
                </div>
                <div class="d-flex justify-content-between align-items-center mb-4">
                  <p class="lead fw-normal mb-0">Liked Movies</p>
                  <p class="mb-0"><a href="#!" class="text-muted">Show all</a></p>
                </div>
                <div class="row g-2">
                  <div class="col mb-2">
                    <img src="https://image.tmdb.org/t/p/original/mSCY3bmb3zV0eBfabUgjJPNLZ3p.jpg"
                      alt="image 1" class="w-100 rounded-3">
                  </div>
                  <div class="col mb-2">
                    <img src="https://image.tmdb.org/t/p/original/8AE7M2lMsyvowfT36porzGtmOtI.jpg"
                      alt="image 1" class="w-100 rounded-3">
                  </div>
                </div>
                <div class="row g-2">
                  <div class="col">
                    <img src="https://image.tmdb.org/t/p/original/6G6nqSW9S7EHA9HrYl0Z8uo2H7f.jpg"
                      alt="image 1" class="w-100 rounded-3">
                  </div>
                  <div class="col">
                    <img src="https://image.tmdb.org/t/p/original/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg"
                      alt="image 1" class="w-100 rounded-3">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>


<script>
export default {
  name: 'UserInfo',
  data() {
    return {
      user: this.$store.state.user
    }
  },
}
</script>

<style>

</style>
