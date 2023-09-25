from typing import Iterable

from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy import text

from sqlalchemy.orm import Session, joinedload
from sqlalchemy.orm import selectinload

import config
from models import Base, User, Address

engine = create_engine(
    url=config.SQLALCHEMY_URL,
    echo=config.SQLALCHEMY_ECHO
)


def create_user_with_emails(session: Session, name: str, username: str, emails: list[str] | None) -> User:
    user = User(
        name=name,
        username=username
    )

    if emails is not None:
        addresses = [
            Address(email=email)
            for email in emails
        ]
        user.addresses = addresses

    session.add(user)
    session.commit()

    return user


def fetch_user(session: Session, name: str) -> User:
    stmt = select(User).where(User.name == name)
    # user: User | None = session.execute(stmt).scalar_one_or_none()
    user: User | None = session.execute(stmt).scalar_one()
    return user


def add_addresses(session: Session, user: User, *emails: str) -> None:
    user.addresses = [
        Address(email=email)
        for email in emails
    ]
    session.commit()


def show_users(session: Session):
    stmt = select(User).options(
        selectinload(User.addresses)
    )
    users: Iterable[User] = session.scalars(stmt)
    for user in users:
        print("[+]", user)
        for address in user.addresses:  # type: Address
            print(" - @", address.email)


def show_addresses(session: Session):
    stmt = select(Address).options(
        joinedload(Address.user)
    )
    addresses: Iterable[Address] = session.scalars(stmt)

    for address in addresses:
        print("[@]", address.email)
        print(" +", address.user)




def main():
    Base.metadata.create_all(bind=engine)

    with Session(engine) as session:
        # res = session.execute(text("SELECT 1;"))
        # print(res.all())
        # create_user_with_emails(session=session, name="Bob White",
        #                         username="bob", emails=None)
        #
        # create_user_with_emails(session=session, name="John Smith",
        #                         username="john",
        #                         emails=[
        #                             "jone@gmail.com",
        #                             "jone.smith@gmail.gov"
        #                         ])

        # user = fetch_user(session, "Bob White")
        # print("bob?", user)
        # add_addresses(session, user, "bob@example.com")
        show_users(session)
        show_addresses(session)




if __name__ == '__main__':
    main()
