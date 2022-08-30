from dagster import (make_values_resource, Field, Array, logger, op, Any, Int, String,
                     file_relative_path, Shape, config_from_files)


def main_config_schema():
    demo_gr = Field(Shape({
        "source_dir": Field(String, is_required=True),
        "destination_dir": Field(String, is_required=True),
        "limit": Field(Int, is_required=False, default_value=3),
    }))

    resource_def = make_values_resource(
        demo_config_group=demo_gr,
    )

    schema = {
        "main_config": resource_def
    }

    return schema


def get_main_config():
    configurations = config_from_files([
        file_relative_path(__file__,
                           'config/main.yaml')
    ]
    )

    return configurations
