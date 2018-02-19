import boto3

client = boto3.client('translate')
text = """     INT. REBEL BLOCKADE RUNNER - MAIN PASSAGEWAY
               An explosion rocks the ship as two robots, Artoo-Detoo (R2-
               D2) and See-Threepio (C-3PO) struggle to make their way
               through the shaking, bouncing passageway. Both robots are
               old and battered. Artoo is a short, claw-armed tripod. His
               face is a mass of computer lights surrounding a radar eye.
               Threepio, on the other hand, is a tall, slender robot of
               human proportions. He has a gleaming bronze-like metallic
               surface of an Art Deco design.

               Another blast shakes them as they struggle along their way.

                                     THREEPIO
                         Did you hear that? They've shut down
                         the main reactor. We'll be destroyed
                         for sure. This is madness!"""
print(len(text))
response = client.translate_text(   Text=text,
                                    SourceLanguageCode='en',
                                    TargetLanguageCode='de')

print(response['TranslatedText'].encode('utf-8'))
# Arabic (ar)
# Chinese (Simplified) (zh)
# French (fr)
# German (de)
# Portuguese (pt)
# Spanish (es)
