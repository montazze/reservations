require 'spec_helper'

context 'table operations' do
  before do
    @eq_model.update_attribute('ordering', 1)
    @eq_model2.update_attribute('ordering', 2)
    @eq_model3.update_attribute('ordering', 3)
    expect(@eq_model.ordering).to eq(1)
    expect(@eq_model2.ordering).to eq(2)
    expect(@eq_model3.ordering).to eq(3)
    sign_in_as_user @superuser
    visit category_equipment_models_path(@category.id)
  end
  after { sign_out }
  it 'swaps orderings and preserves neutral elements' do
    first('.glyphicon-arrow-down').click
    expect(@eq_model.reload.ordering).to eq(2)
    expect(@eq_model2.reload.ordering).to eq(1)
    expect(@eq_model3.reload.ordering).to eq(3)
  end
  it 'does not allow priority above 1' do
    first('.glyphicon-arrow-up').click
    expect(@eq_model.reload.ordering).to eq(1)
    expect(@eq_model2.reload.ordering).to eq(2)
    expect(@eq_model3.reload.ordering).to eq(3)
  end
  it 'does not allow priority below number of elements' do
    all('.glyphicon-arrow-down').last.click
    expect(@eq_model.reload.ordering).to eq(1)
    expect(@eq_model2.reload.ordering).to eq(2)
    expect(@eq_model3.reload.ordering).to eq(3)
  end
end
