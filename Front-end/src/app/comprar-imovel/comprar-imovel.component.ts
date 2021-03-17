import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api-service.service';

@Component({
  selector: 'app-comprar-imovel',
  templateUrl: './comprar-imovel.component.html',
  styleUrls: ['./comprar-imovel.component.scss']
})
export class ComprarImovelComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {}

  insereNovoCliente
    (
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
        "pessoa":
        {
          "nome": nome,
          "cpf": cpf,
          "data_nasc": data_nasc,
          "rg": rg,
          "profissao": profissao,
          "estado_civil": estado_civil,
        },
        "endereco":
        {
          "rua": rua_prop,
          "numero": numero_prop,
          "andar": andar_prop,
          "bloco": bloco_prop,
          "bairro": bairro_prop,
          "cep": cep_prop,
          "cidade": cidade_prop,
          "uf": uf_prop,
        },
      }).subscribe(data => {
      console.log(data)
    },
    error  => {
      console.log("Error", error);
      console.log(data_nasc)
    });
  }
}
