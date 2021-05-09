<template>
  <div class="hello">
    <input type="file" @change="onFileSelected" /> 
    <button @click="onUpload">Upload</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "welcome to the user app",
    };
  },
  methods: {
    onFileSelected(event) {
      this.selectedFile = event.target.files[0]
    }, 
    onUpload() {
      const fd = new FormData();
      fd.append('image', this.selectedFile,this.selectedFile.name)
      axios.post('http://127.0.0.1:8000/sakujoooCloud/',fd,{
        onUploadProgress: uploadEvent=>{
          console.log('Upload Progress:'+Math.round(uploadEvent.loaded/uploadEvent.total *100+'%'))

        }
      }).then(res=>{
        console.log(res)
      });

    }
  },
};
</script>

<style lang="scss" scoped>
</style>
</style>