const listaTodos = document.querySelector('#lista-todos');
const button = document.querySelector('#button-todos');

async function pedirTodos() {
  const response = await fetch('http://localhost:8000/todos/');
  const data = await response.json();
  let todos = '';
  listaTodos.innerHTML = data.map(todo => `<li>${todo.title}</li>`).join('\n');
}

button.addEventListener('click', pedirTodos);
