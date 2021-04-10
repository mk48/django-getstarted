# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountYear(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    shop = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_year'
        unique_together = (('shop', 'name'),)


class Company(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    old_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=75)
    created_by = models.ForeignKey(
        'User', models.DO_NOTHING, related_name='+', db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey(
        'User', models.DO_NOTHING, related_name='+', db_column='updated_by', blank=True, null=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Medicine(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    old_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=75)
    hsn = models.BigIntegerField(blank=True, null=True)
    packing = models.SmallIntegerField(blank=True, null=True)
    gst = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    is_schedule = models.BooleanField(blank=True, null=True)
    is_available = models.BooleanField(blank=True, null=True)
    rack_no = models.CharField(max_length=5, blank=True, null=True)
    box_no = models.CharField(max_length=5, blank=True, null=True)
    is_expirable = models.BooleanField(blank=True, null=True)
    is_nrx = models.BooleanField(blank=True, null=True)
    is_life_saving_drug = models.BooleanField(blank=True, null=True)
    minstock = models.SmallIntegerField(blank=True, null=True)
    created_by = models.ForeignKey(
        'User', models.DO_NOTHING, related_name='+', db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey(
        'User', models.DO_NOTHING,  related_name='+', db_column='updated_by', blank=True, null=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True)
    medicinetype = models.ForeignKey(
        'MedicineType', models.DO_NOTHING, blank=True, null=True)
    medicinegroup = models.ForeignKey(
        'MedicineGroup', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicine'


class MedicineGroup(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    old_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=75)
    created_by = models.ForeignKey(
        'User', models.DO_NOTHING,  related_name='+', db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey(
        'User', models.DO_NOTHING,  related_name='+', db_column='updated_by', blank=True, null=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicine_group'


class MedicineType(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    old_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=75)
    created_by = models.ForeignKey(
        'User', models.DO_NOTHING,  related_name='+', db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey(
        'User', models.DO_NOTHING,  related_name='+', db_column='updated_by', blank=True, null=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicine_type'


class Openingstock(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    old_srno = models.IntegerField(blank=True, null=True)
    batch_no = models.CharField(max_length=50)
    prp = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    mrp_per_pack = models.DecimalField(max_digits=8, decimal_places=2)
    gst = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    expiry_date = models.DateField()
    single_qty = models.SmallIntegerField()
    old_purbillno = models.IntegerField(blank=True, null=True)
    old_billdate = models.DateField(blank=True, null=True)
    old_invno = models.CharField(max_length=20)
    prdv = models.DecimalField(max_digits=8, decimal_places=2)
    rate_pure = models.DecimalField(max_digits=8, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    rate_with_discount = models.DecimalField(max_digits=8, decimal_places=2)
    created_by = models.ForeignKey(
        'User', models.DO_NOTHING,  related_name='+', db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey(
        'User', models.DO_NOTHING,  related_name='+', db_column='updated_by', blank=True, null=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True)
    medicine = models.ForeignKey(
        Medicine, models.DO_NOTHING, blank=True, null=True)
    old_supplier = models.ForeignKey(
        'Supplier', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openingstock'


class PurchaseGst(models.Model):
    id = models.UUIDField(primary_key=True)
    gst = models.DecimalField(max_digits=4, decimal_places=2)
    taxable = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    purchase_main = models.ForeignKey(
        'PurchaseMain', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_gst'


class PurchaseMain(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    old_id = models.IntegerField(blank=True, null=True)
    billno = models.SmallIntegerField()
    purchase_date = models.DateField()
    bill_date = models.DateField()
    inv_no = models.CharField(max_length=20)
    is_paymethod_cash = models.BooleanField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    adjustment_amount = models.DecimalField(max_digits=8, decimal_places=2)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(
        'User', models.DO_NOTHING,  related_name='+', db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey(
        'User', models.DO_NOTHING,  related_name='+', db_column='updated_by', blank=True, null=True)
    account_year = models.ForeignKey(
        AccountYear, models.DO_NOTHING, blank=True, null=True)
    supplier = models.ForeignKey(
        'Supplier', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_main'


class PurchaseSub(models.Model):
    id = models.UUIDField(primary_key=True)
    srno = models.SmallIntegerField()
    batch_no = models.CharField(max_length=50)
    expiry_date = models.DateField()
    mrp_per_pack = models.DecimalField(max_digits=8, decimal_places=2)
    rate_pure = models.DecimalField(max_digits=8, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    rate_with_discount = models.DecimalField(max_digits=8, decimal_places=2)
    gst = models.DecimalField(max_digits=4, decimal_places=2)
    c_gst_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    c_gst_amount = models.DecimalField(max_digits=8, decimal_places=2)
    s_gst_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    s_gst_amount = models.DecimalField(max_digits=8, decimal_places=2)
    prdv = models.DecimalField(max_digits=8, decimal_places=2)
    prp = models.DecimalField(max_digits=8, decimal_places=2)
    qty_strip = models.SmallIntegerField()
    free_qty_strip = models.SmallIntegerField()
    is_replace = models.BooleanField()
    is_return_product = models.BooleanField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    purchase_main = models.ForeignKey(
        PurchaseMain, models.DO_NOTHING, blank=True, null=True)
    medicine = models.ForeignKey(
        Medicine, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_sub'


class Session(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    account_year = models.ForeignKey(
        AccountYear, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session'


class Shop(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop'


class Supplier(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    old_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=75)
    tin = models.CharField(max_length=20, blank=True, null=True)
    gst_no = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(
        'User', models.DO_NOTHING,  related_name='+', db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey(
        'User', models.DO_NOTHING,  related_name='+', db_column='updated_by', blank=True, null=True)
    shop = models.ForeignKey(Shop, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'user'


class UserAccountYear(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    account_year = models.ForeignKey(
        AccountYear, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_account_year'
        unique_together = (('user', 'account_year'),)
