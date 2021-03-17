import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListarImoveisComponent } from './listar-imoveis/listar-imoveis.component';
import { NovoImovelComponent } from './novo-imovel/novo-imovel.component';
import { ComprarImovelComponent } from './comprar-imovel/comprar-imovel.component';

const routes: Routes = [
  {path:'listar-imoveis', component: ListarImoveisComponent},
  {path:'novo-imovel', component: NovoImovelComponent},
  {path:'comprar-imovel', component: ComprarImovelComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
