import { Component, OnInit } from '@angular/core';
import { ApiServiceService } from '../services/api-service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  imoveis:any; //{[index:string]:any} = {}
  pessoas:any;
  clientes:any;
  enderecos:any;
  tipos:any;
  gastos:any;
  id_tipo:any;


  constructor(private apiService: ApiServiceService) { }

  ngOnInit() {
    this.apiService.getImoveis().subscribe((data)=>{
      // console.log(data);
      this.imoveis = data; //TODO: Verificar
      // console.log(this.imoveis[0])
    });

    this.apiService.getPessoas().subscribe((data)=>{
      this.pessoas = data; //TODO: Verificar
      // console.log(this.pessoas[0])
    });

    this.apiService.getClientes().subscribe((data)=>{
      this.clientes = data; //TODO: Verificar
      // console.log(this.clientes[0])
    });

    this.apiService.getImoveis().subscribe((data)=>{
      this.imoveis = data; //TODO: Verificar
      // console.log(this.imoveis[0])
    });

    this.apiService.getEndereços().subscribe((data)=>{
      this.enderecos = data; //TODO: Verificar
      // console.log(this.enderecos[0])
    });

    this.apiService.getTipos().subscribe((data) =>{
      this.tipos = data;
      console.log(data)
    });

    this.apiService.getGastos().subscribe((data) =>{
      this.gastos = data;
      console.log(data)
    });
  }

  insereNovoCliente
    (
    rua_imovel: string,
    numero_imovel: string,
    andar_imovel: string,
    bloco_imovel: string,
    bairro_imovel: string,
    cep_imovel: string,
    cidade_imovel: string,
    uf_imovel: string,
    idade: string,
    id_tipo: string,
    energia: string,
    agua: string,
    condominio: string,
    propaganda:string,
    nome: string,
    cpf: string,
    data_nasc: string,
    rg: string,
    profissao: string ,
    estado_civil: string,
    rua_prop: string,
    numero_prop: string,
    andar_prop: string,
    bloco_prop: string,
    bairro_prop: string,
    cep_prop: string,
    cidade_prop: string,
    uf_prop: string,
    )
    {
    this.apiService.postCliente({
      "endereco": {
        "rua": rua_imovel,
        "numero": numero_imovel,
        "andar": andar_imovel,
        "bloco": bloco_imovel,
        "bairro": bairro_imovel,
        "cep": cep_imovel,
        "cidade": cidade_imovel,
        "uf": uf_imovel,
      },
      "id_tipo": id_tipo,
      "gastos": {
        "energia": energia,
        "agua": agua,
        "condominio": condominio,
        "propaganda": propaganda,
      },
      "idade": idade,
      "proprietario": {
        "pessoa": {
          "nome": nome,
          "cpf": cpf,
          "data_nasc": data_nasc,
          "rg": rg,
          "profissao": profissao,
          "estado_civil": estado_civil,
        },
        "endereco": {
          "rua": rua_prop,
          "numero": numero_prop,
          "andar": andar_prop,
          "bloco": bloco_prop,
          "bairro": bairro_prop,
          "cep": cep_prop,
          "cidade": cidade_prop,
          "uf": uf_prop,
        }
      }
    }).subscribe(data => {
      console.log(data)
    },
    error  => {
    console.log("Error", error);
    });
  }

  insereNovaPessoa(
      nome: string,
      cpf: string,
      data_nasc: string,
      rg: string,
      profissao: string ,
      estado_civil: string
    ){
    this.apiService.postPessoa({
      "nome": nome,
      "cpf": cpf,
      "data_nasc": data_nasc,
      "rg": rg,
      "profissao": profissao,
      "estado_civil": estado_civil
    }).subscribe(data => {
      console.log(data);
    },
    error  => {
    console.log("Error", error);
    });
  }
}
