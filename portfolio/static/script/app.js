let comment_blog = document.querySelector("#comment_blog");
let comment_img = document.querySelector("#comment_img");
let burger = document.querySelector("#burger");
let nav_list = document.querySelector(".nav_list");
let form_mes = document.querySelector("#post-form-message");
let mes = document.querySelector("#id_value");

if (comment_img) {
  comment_img.onclick = () => {
    comment_blog.classList.toggle("hidden");
  };
}
burger.onclick = () => {
  nav_list.classList.toggle("tab:hidden");
  console.log("jgjhghj");
 
};
form_mes.onsubmit = (e) => {
  e.preventDefault()
  console.log("cliced hhhhh", e.target);
  let newO = {
    value: e.target["value"].value,
    user: e.target["user"].value,
    room: e.target["room"].value,
    username: e.target["username"].value,
  };

  console.log(">>",newO)
  const post = async () => {
    const { data } = await axios.post(
      `/chat//?username=mustafo_2003`,
      newO
    );
  }
  post()
  mes.value = ''
}
