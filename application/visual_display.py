from tkinter import Tk, Canvas

def create_animation(success_rate, test_environment, config):
    test_environment.generation_animation = Tk()
    test_environment.canvas = Canvas(test_environment.generation_animation, width = config.render_spaces_width * test_environment.wide, height = config.render_spaces_width * test_environment.high)
    test_environment.canvas.pack()
    gen_text_display = "Generation - %s" %(test_environment.generation_number)
    stats_text_display = "Success rate - %s" %(success_rate)
    test_environment.canvas.create_text(5,5,fill="black",font="Courier 16", text=gen_text_display, anchor="nw")
    test_environment.canvas.create_text(5,18,fill="black",font="Courier 16", text=stats_text_display, anchor="nw")

def draw_target(canvas, x, y, square_width, **kwargs):
    square_centre_x = (square_width * x) + (square_width / 2)
    square_centre_y = (square_width * y) + (square_width / 2)
    return canvas.create_rectangle(square_centre_x - (square_width / 2), square_centre_y - (square_width / 2), square_centre_x + (square_width / 2), square_centre_y + (square_width / 2), **kwargs)

def draw_robot(canvas, x, y, r, **kwargs):
    return canvas.create_arc(x-r, y-r, x+r, y+r, **kwargs)

def draw_projectile(canvas, x, y, r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def move_object(canvas, object_to_move, x, y, circle_radius, square_width):
    circ_centre_x = (square_width * x) + square_width / 2
    circ_centre_y = (square_width * y) + square_width / 2
    canvas.coords(object_to_move, circ_centre_x-circle_radius, circ_centre_y-circle_radius, circ_centre_x+circle_radius, circ_centre_y+circle_radius)

def change_robot_canvas_direction(canvas, robot, current_arc_start):
    new_arc_start = current_arc_start    #arc starts at east on default
    if robot.facing == 'north':
        new_arc_start = current_arc_start + 90
    elif robot.facing == 'west':
        new_arc_start = current_arc_start + 180
    elif robot.facing == 'south':
        new_arc_start = current_arc_start + 270
    canvas.itemconfigure(robot.canvas_shape, start=new_arc_start)

def remove_shapes_from_canvas(test_environment):
    shapes_to_remove = test_environment.canvas_shapes_to_remove
    for shape in shapes_to_remove:
        test_environment.canvas.delete(shape)

def animate_move(test_environment, config):
    remove_shapes_from_canvas(test_environment)
    test_environment.generation_animation.title("Generation - %s" %('chasing_target'))
    draw_all_targets(test_environment, config)
    draw_all_projectiles(test_environment, config)
    draw_all_robots(test_environment, config)
    test_environment.generation_animation.update()

#When drawing all targets, you will need to compute their y distance on canvas as test_environment.high - object.y
#This is because my simulation uses a cartesian grid, starting at bottom left, but Tkinter draws from top left.

def draw_all_targets(test_environment, config):
    for target in test_environment.targets_in_test_environment:
        square_width = config.render_spaces_width
        distance_from_bottom = test_environment.high - (target.y + 1)
        if target.canvas_shape == None:
            target.canvas_shape = draw_target(test_environment.canvas, target.x, distance_from_bottom, config.render_spaces_width, fill=target.colour)

def draw_all_projectiles(test_environment, config):
    for projectile in test_environment.projectiles_in_test_environment:
        square_width = config.render_spaces_width
        circle_radius = config.render_spaces_width/7
        distance_from_bottom = test_environment.high - (projectile.y + 1)
        if projectile.canvas_shape == None:
            projectile.canvas_shape = draw_projectile(test_environment.canvas, projectile.x, distance_from_bottom, circle_radius, fill=projectile.colour)
        move_object(test_environment.canvas, projectile.canvas_shape, projectile.x, distance_from_bottom, circle_radius, square_width)

def draw_all_robots(test_environment, config):
    for robot in test_environment.robots_in_test_environment:
        square_width = config.render_spaces_width
        circle_radius = config.render_spaces_width/2
        distance_from_bottom = test_environment.high - (robot.y + 1)
        if robot.canvas_shape == None:
            robot.canvas_shape = draw_robot(test_environment.canvas, robot.x, distance_from_bottom, circle_radius, fill=robot.colour, start=config.robot_arc_start, extent=config.robot_arc_extent)
        move_object(test_environment.canvas, robot.canvas_shape, robot.x, distance_from_bottom, circle_radius, square_width)
        change_robot_canvas_direction(test_environment.canvas, robot, config.robot_arc_start)