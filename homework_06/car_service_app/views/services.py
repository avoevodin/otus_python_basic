import logging

from flask import Blueprint, render_template, request, flash, url_for, redirect
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import NotFound, InternalServerError

from models import Service, db
from views.forms import ServiceForm

log = logging.getLogger(__name__)
services_app = Blueprint("services_app", __name__)


@services_app.get("/", endpoint="list")
def get_services_list():
    services = Service.query.all()
    return render_template("services/list.html", services=services)


@services_app.route("/<int:service_id>", methods=["GET", "DELETE"], endpoint="details")
def get_service_by_id(service_id: int):
    service = Service.query.get(service_id)
    if not service:
        raise NotFound(f"Service #{service_id} not found!")

    if request.method == "GET":
        return render_template("services/details.html", service=service)

    service_name = service.name
    db.session.delete(service)
    db.session.commit()
    flash(f"Deleted service #{service_id} {service_name!r}", "warning")
    url = url_for("services_app.list")
    return {"ok": True, "url": url}


@services_app.route("/add", methods=["GET", "POST"], endpoint="add")
def add_service():
    form = ServiceForm()

    if request.method == "GET":
        return render_template("services/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("services/add.html", form=form), 400

    service_name = form.name.data
    service_description = form.description.data
    service_image = form.image.data
    service_free_car_wash = form.free_car_wash.data

    service = Service(
        name=service_name,
        description=service_description,
        image=service_image,
        free_car_wash=service_free_car_wash,
    )

    db.session.add(service)

    try:
        db.session.commit()
    except IntegrityError:
        error_text = (
            f"Could not save service {service_name!r}, probably name is not unique!"
        )
        form.form_errors.append(error_text)
        return render_template("services/add.html", form=form), 400
    except DatabaseError:
        log.exception("Could not save service %r", service_name)
        raise InternalServerError(f"Could not save service {service_name!r}")

    flash(f"Created new service: {service_name!r}", "success")
    print(service.id)
    url = url_for("services_app.details", service_id=service.id)
    return redirect(url)
