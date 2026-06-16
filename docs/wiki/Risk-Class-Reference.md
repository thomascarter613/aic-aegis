# Risk Class Reference

Tool and action risk classes.

---

## Risk Classes

| Class          | Meaning                                                |
| -------------- | ------------------------------------------------------ |
| `read_only`    | Reads without mutation                                 |
| `low_write`    | Draft or suggestion                                    |
| `medium_write` | Non-critical mutation                                  |
| `high_write`   | External or important action                           |
| `critical`     | Destructive, legal, financial, regulated, irreversible |

---

## MVP Rule

`email.send` is `high_write` and must be denied or approval-gated.

---

## North Star

Risk classes help Aegis govern tool use proportionally.

---