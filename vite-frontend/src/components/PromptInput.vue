<template>
  <div>
    <div v-if="formSubmitted">
      <hr />
      <p>prompt: {{ prompt }}</p>
      <div v-if="answer">
        <!-- <p v-bind:src="response" >{{ response }}</p> -->
        <p>{{ response }}</p>
      </div>
      <div v-else>
        <h2>hmm...</h2>
      </div>
    </div>

    <form @submit.prevent="submitForm">
      <br />
      <input
        type="text"
        v-model="prompt"
        placeholder="input the prompt"
        required
      />
      <br /><br />
      <button type="submit" class="submit button" role="button">
        Submit
      </button>
    </form>
  </div>
</template>
<script>
export default {
  data() {
    return {
      prompt: "",
      formSubmitted: false,
      answer: null,
    };
  },

  methods: {
    submitForm: function () {
      this.formSubmitted = true;
      try {
        fetch("http://127.0.0.1:8000/ai/" + this.prompt)
          .then((response) => {
            console.log(response)
            return response.json();
          })
          .then((data) => {
            console.log(data["answer"]);
            this.answer = data["answer"];
          });
      } catch (error) {
        console.log(error);
      }
    },

    //sending prompt to Google api
  },

  computed: {
    response() {
      return this.answer;
    },
  },
};
</script>

<style scoped>

/* CSS */

</style>