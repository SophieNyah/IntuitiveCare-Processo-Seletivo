<template id="parameters">
  <header>
      Pesquise uma operadora
  </header>

  <div class="center">
    <div class="space">
      <p>Identificador</p>
      <input v-model="operadora" placeholder="E-VIDA" />
    </div>

    <div class="space">
      <div>Tipo de Pesquisa</div>
      <select v-model="tipo">
        <option value="corporate_name">Razão Social</option>
        <option value="commercial_name">Nome Fantasia</option>
      </select>
    </div>

    <div class="space">
        <button @click="search()">Buscar</button>
    </div>
  </div>

    <Operadoras v-show="isModalVisible" @close="closeModal">
        <template v-slot:header>Operadoras</template>
        <template v-slot:body>
            <span v-if="found_operadoras?.length == 0">Nenhuma operadora `{{operadora}}` encontrada.</span>
            <span v-else>
                <p v-for="item in found_operadoras">
                  <p><b>Registro ANS:</b> {{item['Registro ANS']}}</p>
                  <p><b>CNPJ:</b> {{item['CNPJ']}}</p>
                  <p><b>Razão Social:</b> {{item['Razão Social']}}</p>
                  <p><b>Nome Fantasia:</b> {{item['Nome Fantasia']}}</p>
                  <p><b>Modalidade:</b> {{item['Modalidade']}}</p>
                  <p><b>Logradouro:</b> {{item['Logradouro']}}</p>
                  <p><b>Número:</b> {{item['Número']}}</p>
                  <p><b>Complemento:</b> {{item['Complemento']}}</p>
                  <p><b>Bairro:</b> {{item['Bairro']}}</p>
                  <p><b>Cidade:</b> {{item['Cidade']}}</p>
                  <p><b>UF:</b> {{item['UF']}}</p>
                  <p><b>CEP:</b> {{item['CEP']}}</p>
                  <p><b>DDD:</b> {{item['DDD']}}</p>
                  <p><b>Telefone:</b> {{item['Telefone']}}</p>
                  <p><b>Fax:</b> {{item['Fax']}}</p>
                  <p><b>Endereço eletrônico:</b> {{item['Endereço eletrônico']}}</p>
                  <p><b>Representante:</b> {{item['Representante']}}</p>
                  <p><b>Representante:</b> {{item['Representante']}}</p>
                  <p><b>Data Registro ANS:</b> {{item['Data Registro ANS']}}</p>
                  <br/><hr><br/>
                </p>
            </span>
        </template>
    </Operadoras>

</template>

<script lang="ts">
import axios from "axios";
import Operadoras from "./components/Operadoras.vue";
export default {
    name: 'App',
    components: { Operadoras },
    data() {
        return {
            operadora: '',
            tipo: 'commercial_name',
            isModalVisible: false,
            found_operadoras: []
        }
    },
    methods: {
        search: function () {
            const API_URL = 'http://sophienyah.pythonanywhere.com/'
            let route = ''
            this.isModalVisible = true
            switch (this.tipo) {
                case 'corporate_name':
                    route = 'razao/'
                    break
                case 'commercial_name':
                    route = 'nome/'
                    break;
            }
            axios
                .get(API_URL + route + this.operadora)
                .then( response => {
                    const data = response.data

                    // Servidor retorna dados na forma
                    //   [{'Nome fantasia': {1664: 'E-VIDA'}, ...}],
                    //   onde o número é o id da linha no dataframe.
                    // O código abaixo retira esse número
                    for(let i=0; i<data.length; i++) {
                        const inner_key = Object.keys(data[i]['Razão Social'])[0]
                        for (let key in data[i]) {
                            data[i][key] = data[i][key][inner_key]
                        }
                    }
                    this.found_operadoras = data
                })
                .catch( err => {})
        },
        closeModal() {
            this.isModalVisible = false
            this.found_operadoras = []
        }
    }
}
</script>

<style scoped>
  header {
    line-height: 1.5;
  }

  button {
      width: 80%;
  }

  .space {
      padding: 10px;
  }

  .center {
    text-align: center;
  }

  @media (min-width: 1024px) {
    header {
      display: flex;
      place-items: center;
      padding-right: calc(var(--section-gap) / 2);
    }

    .logo {
      margin: 0 2rem 0 0;
    }

    header .wrapper {
      display: flex;
      place-items: flex-start;
      flex-wrap: wrap;
    }
  }
</style>
