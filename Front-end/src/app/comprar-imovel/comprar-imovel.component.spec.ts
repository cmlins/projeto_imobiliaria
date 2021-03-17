import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComprarImovelComponent } from './comprar-imovel.component';

describe('ComprarImovelComponent', () => {
  let component: ComprarImovelComponent;
  let fixture: ComponentFixture<ComprarImovelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ComprarImovelComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ComprarImovelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
