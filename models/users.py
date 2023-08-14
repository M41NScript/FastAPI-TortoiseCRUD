from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True, generated=True)
    name = fields.CharField(max_length=128)
    username = fields.CharField(max_length=32, unique=True, null=True)
    email = fields.CharField(max_length=128, unique=True)
    password = fields.CharField(max_length=256)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    class Meta:
        table = "Users"
        ordering = ["-created_at"]
    
    def __str__(self) -> str:
        return self.email
    
