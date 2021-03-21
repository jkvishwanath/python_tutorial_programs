import logging
import logging.handlers
import smtplib
import string  # for tls add this line


class TlsSMTPHandler(logging.handlers.SMTPHandler):
    def emit(self, record):
        """
        Emit a record.

        Format the record and send it to the specified addressees.
        """
        try:
            try:
                from email.utils import formatdate
            except ImportError:
                formatdate = self.date_time
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP(self.mailhost, port)
            msg = self.format(record)
            msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
                self.fromaddr,
                self.toaddrs,
#                ''.join(self.toaddrs, ","),
                self.getSubject(record),
                formatdate(), msg)
            if self.username:
                smtp.ehlo()  # for tls add this line
                smtp.starttls()  # for tls add this line
                smtp.ehlo()  # for tls add this line
                smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


logger = logging.getLogger()

gm = TlsSMTPHandler(("smtp.gmail.com", 587), 'bugs@my_company.com', ['admin@my_company.com'], 'Error found!',
                    ('your_email@gmail.com', 'your_password'))
gm.setLevel(logging.ERROR)

logger.addHandler(gm)

try:
    1 / 0
except:
    logger.exception('FFFFFFFFFFFFFFFFFFFFFFFUUUUUUUUUUUUUUUUUUUUUU-')
