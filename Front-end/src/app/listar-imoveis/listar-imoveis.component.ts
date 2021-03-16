import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api-service.service';

@Component({
  selector: 'app-listar-imoveis',
  templateUrl: './listar-imoveis.component.html',
  styleUrls: ['./listar-imoveis.component.scss']
})
export class ListarImoveisComponent implements OnInit {
  imoveis:any; //{[index:string]:any} = {}
  pessoas:any;
  clientes:any;
  enderecos:any;
  tipos:any;
  gastos:any;

  constructor(private apiService: ApiService) { }

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
}
