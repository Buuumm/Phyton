from rest_framework import serializers

from wypozyczsam_app.wypozyczsam_app.wypozyczsam_app.models import rezerwacja, administrator, klient, auto


class klientSerializer(serializers.ModelSerializer):
    class Meta:
        model = klient
        fields = ["idklient", "nazwisko", "login", "haslo", "email", "nr_prawojazdy"]

        def validate_login(self, login):
            if not login or not login.isalpha():
                raise serializers.ValidationError("Login cannot be empty field")

        def validate_email(self, email):
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not (re.search(regex, email)):
                raise serializers.ValidationError("Wrong email format!")
            else:
                return email

        def validate_password(self, haslo):
            if len(haslo) < 8:
                raise serializers.ValidationError("Make sure your password is at lest 8 letters")
            elif re.search('[0-9]', haslo) is None:
                raise serializers.ValidationError("Make sure your password has a number in it")
            elif re.search('[A-Z]', haslo) is None:
                raise serializers.ValidationError("Make sure your password has a capital letter in it")
            else:
                return haslo

        def validate_surname(self, nazwisko):
            if not nazwisko or not nazwisko.isalpha():
                raise serializers.ValidationError("Surname cannot be empty field")
            return nazwisko.title()

        def validate_prawo(self, nr_prawojazdy):
            if not adres:
                raise serializers.ValidationError("You must type something!")
            elif len(adres) > 45:
                raise serializers.ValidationError("Your comment can only have 45 letters!")
            else:
                return adres

class autoSerializer(serializers.ModelSerializer):
    class Meta:
        model = auto
        fields = ["nr_placowy", "mark", "model", "rocznik", "przebieg"]

    def validate_przebieg(self, przebieg):
        if not przebieg
            raise serializers.ValidationError("You must type something!")
        elif len(przebieg) > 45:
            raise serializers.ValidationError("Your comment can only have 45 letters!")
        else:
            return przebieg

    def validate_cena(self, nr_placowy):
        if not nr_placowy:
            raise serializers.ValidationError("You must type something!")
        return nr_placowy

class zamowieniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = rezerwacja
        fields = ["idrezerwacja", "nr_placowy", "idklient","data_wypozyczenia", "data_zwrotu","cena"]


class uzytkownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = administrator
        fields = ["idadministrator", "login", "haslo"]

        def validate_password(self, haslo):
            if len(haslo) < 8:
                raise serializers.ValidationError("Make sure your password is at lest 8 letters")
            elif re.search('[0-9]', haslo) is None:
                raise serializers.ValidationError("Make sure your password has a number in it")
            elif re.search('[A-Z]', haslo) is None:
                raise serializers.ValidationError("Make sure your password has a capital letter in it")
            else:
                return haslo

        def validate_login(self, login):
            if not login or not login.isalpha():
                raise serializers.ValidationError("Login cannot be empty field")