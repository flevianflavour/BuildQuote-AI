from calculator import generate_estimate


class EstimationService:

    def estimate(self, project):

        return generate_estimate(
            county=project.county,
            project_type=project.house_type,
            length=project.length,
            width=project.width,
            wall_height=project.height,
            block_type=project.wall_material,
            doors=2,
            windows=4,
        )