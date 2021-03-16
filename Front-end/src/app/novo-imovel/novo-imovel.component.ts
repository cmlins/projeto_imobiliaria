import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api-service.service';

@Component({
  selector: 'app-novo-imovel',
  templateUrl: './novo-imovel.component.html',
  styleUrls: ['./novo-imovel.component.scss']
})
export class NovoImovelComponent implements OnInit {
  imoveis:any; //{[index:string]:any} = {}
  pessoas:any;
  clientes:any;
  enderecos:any;
  tipos:any;
  gastos:any;
  id_tipo:any;
  title = "Imobiliária Vida Nova"
  isCollapsed = true;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {}

  insereNovoImovel
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
    tipo: string,
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
    this.apiService.postImovel({
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
      "tipo": tipo,
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
        },
      }
    }).subscribe(data => {
      console.log(data_nasc)
      console.log(data)

    },
    error  => {
      console.log("Error", error);

      console.log(data_nasc)
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
