 /**
  * Class translate string from Eng to chosen lang
  * */
class Translater {
     static async TransalteString(str, lang){
        return await translate(str, lang);
    }
}