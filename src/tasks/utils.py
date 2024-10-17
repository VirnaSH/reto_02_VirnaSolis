def validate_ruc(ruc):
  return (len(ruc) == 11 and ruc.isdigit())

# TODO: implementar handle_invalid_ruc()
def handle_invalid_ruc(ruc):
  with open("invalid_ruc.txt", "a") as f:
    f.write(f"{ruc}\n")