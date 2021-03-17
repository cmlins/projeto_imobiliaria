import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api-service.service';

@Component({
  selector: 'app-comprar-imovel',
  templateUrl: './comprar-imovel.component.html',
  styleUrls: ['./comprar-imovel.component.scss']
})
export class ComprarImovelComponent implements OnInit {
  id_imovel:any;
  id_proprietario:any;
  imoveis:any;
  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.apiService.getImoveis().subscribe((data)=>{
      // console.log(data);
      this.imoveis = data;
    });
    // console.log(imovel.id)
  }

  transacaoCompra(
    nome: string,
    cpf: string,
    data_nasc: string,
    rg: string,
    profissao: string,
    estado_civil: string,
    rua_comprador: string,
    numero_comprador: string,
    andar_comprador: string,
    bloco_comprador: string,
    bairro_comprador: string,
    cep_comprador: string,
    cidade_comprador: string,
    uf_comprador: string,
    id_proprietario: string,
    id_imovel: string,
    vista: string,
    banco: string,
    entrada: string,
    parcelas: string,
   ){
     this.apiService.postTransacao({
      "comprador":
      {
        "pessoa":
        {
          "nome": nome,
          "cpf": cpf,
          "data_nasc": data_nasc,
          "rg": rg,
          "profissao": profissao,
          "estado_civil": estado_civil
        },
        "endereco":
        {
          "rua": rua_comprador,
          "numero": numero_comprador,
          "andar": andar_comprador,
          "bloco": bloco_comprador,
          "bairro": bairro_comprador,
          "cep": cep_comprador,
          "cidade": cidade_comprador,
          "uf": uf_comprador
        }
      },
      "id_proprietario": id_proprietario,
      "id_imovel": id_imovel,
      "pagamento":
      {
        "vista": vista,
        "id_banco": banco,
        "entrada": entrada,
        "n_parcelas": parcelas,
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
