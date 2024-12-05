import numpy as np
import random
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def evolution_step(current_state, num_rows, num_cols):
    next_step = np.zeros((num_rows, num_cols))

    for id_row in range(num_rows):
        for id_col in range(num_cols):
            #print("\n"*4 + "+"*10 + f"\n\n\nCell in [{id_row}][{id_col}] ")
            if id_row == 0:
                upper_index = id_row + 1
                lower_index = num_rows - 1
            elif id_row == (num_rows-1):
                upper_index = 0
                lower_index = id_row - 1
            else:
                upper_index = id_row + 1
                lower_index = id_row - 1

            if id_col == 0:
                left_index = num_cols-1
                right_index = id_col + 1
            elif id_col == (num_cols-1):
                left_index = id_col - 1
                right_index = 0
            else:
                left_index = id_col - 1
                right_index = id_col + 1

            counter = 0
            for col_sample in [left_index, id_col, right_index]:
                for row_sample in [lower_index, id_row, upper_index]:
                    if not ((col_sample == id_col) and (row_sample == id_row)):
                        if current_state[row_sample][col_sample]:
                            #print(f"\t\tcounter increased by one thanks to the cell in [{row_sample}][{col_sample}]")
                            counter += current_state[row_sample][col_sample]

            next_step[id_row][id_col] = current_state[id_row][id_col]

            if current_state[id_row][id_col] == 1:
                # The cell is alive
                #print(f"\t\tis alive and the counter is {counter}")
                if (counter < 2) or (counter > 3):
                    next_step[id_row][id_col] = 0

            if current_state[id_row][id_col] == 0:
                # The cell is dead
                #print(f"\t\tis dead and the counter is {counter}")
                if counter == 3:
                    next_step[id_row][id_col] = 1

            #print(f"\t\tin the next step is {next_step[id_row][id_col]}")

    return next_step





def main():
    num_rows = 300
    num_cols = 450

    initial_array = np.zeros((num_rows, num_cols))

    possible_initial_values = [0, 1]

    for id_row in range(num_rows):
        for id_col in range(num_cols):
            initial_array[id_row][id_col] = random.choice(possible_initial_values)

    num_iterations = 5

    current_state = initial_array
    for id_iteration in range(num_iterations):
        #print(id_iteration)
        next_state = evolution_step(
            current_state=current_state,
            num_rows=num_rows,
            num_cols=num_cols
        )

        current_state = next_state

    f, ax = plt.subplots(figsize=(9, 6))
    the_heatmap = sns.heatmap(current_state, cmap="crest", ax=ax)
    plt.show()

def animation_example():
    fig, ax = plt.subplots()
    t = np.linspace(0, 3, 40)
    g = -9.81
    v0 = 12
    z = g * t ** 2 / 2 + v0 * t

    v02 = 5
    z2 = g * t ** 2 / 2 + v02 * t

    scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
    line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
    ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
    ax.legend()

    def update(frame):
        # for each frame, update the data stored on each artist.
        x = t[:frame]
        y = z[:frame]
        # update the scatter plot:
        data = np.stack([x, y]).T
        scat.set_offsets(data)
        # update the line plot:
        line2.set_xdata(t[:frame])
        line2.set_ydata(z2[:frame])
        return (scat, line2)

    ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
    plt.show()

def animation_example_2():
    fig = plt.figure()

    def init():
        sns.heatmap(np.zeros((10, 10)), vmax=.8, square=True, cbar=False)

    def animate(i):
        data = data_list[i]
        sns.heatmap(data, vmax=.8, square=True, cbar=False)

    data_list = []
    for j in range(20):
        data = np.random.rand(10, 10)
        data_list.append(data)

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=20, repeat=False)

    savefile = r"test3.gif"
    pillowwriter = animation.PillowWriter(fps=2)
    anim.save(savefile, writer=pillowwriter)

    plt.show()

def animation_example_2_mod():
    # num_rows = 30
    # num_cols = 70

    num_rows = 100
    num_cols = 150

    initial_array = np.zeros((num_rows, num_cols))

    possible_initial_values = [0, 1]

    # initial_alive = (
    #     (2, 2),
    # )

    # initial_alive = (
    #     (2, 2),  # Center
    #
    #     (1, 1),
    #     (1, 2),
    #     # (1, 3),
    #
    #     # (3, 1),
    #     # (3, 2),
    #     # (3, 3),
    #
    #     # (2, 1),
    #     # (2, 3),
    # )

    # initial_alive = (
    #     (2, 6),
    #     (2, 7),
    #     (3, 6),
    #     (3, 7),
    #     (12, 6),
    #     (12, 7),
    #     (12, 8),
    #     (13, 5),
    #     (13, 9),
    #     (14, 4),
    #     (14, 10),
    #     (15, 4),
    #     (15, 10),
    #     (16, 7),
    #     (17, 5),
    #     (17, 9),
    #     (18, 6),
    #     (18, 7),
    #     (18, 8),
    #     (19, 7),
    #     (22, 4),
    #     (22, 5),
    #     (22, 6),
    #     (23, 4),
    #     (23, 5),
    #     (23, 6),
    #     (24, 3),
    #     (24, 7),
    #     (26, 2),
    #     (26, 3),
    #     (26, 7),
    #     (26, 8),
    #     (36, 4),
    #     (36, 5),
    #     (37, 4),
    #     (37, 5),
    # )
    #
    # for x_pos, y_pos in initial_alive:
    #     initial_array[y_pos+5][x_pos+5] = 1

    for id_row in range(num_rows):
        for id_col in range(num_cols):
            initial_array[id_row][id_col] = random.choice(possible_initial_values)

    num_iterations = 500

    data_list = []

    current_state = initial_array
    for id_iteration in range(num_iterations):
        #print(id_iteration)
        data_list.append(current_state)
        next_state = evolution_step(
            current_state=current_state,
            num_rows=num_rows,
            num_cols=num_cols
        )

        current_state = next_state


    fig = plt.figure()

    def init():
        sns.heatmap(initial_array, vmax=1, square=True, cbar=False) #, linecolor='white', linewidths=1)

    def animate(i):
        data = data_list[i]
        sns.heatmap(data, vmax=1, square=True, cbar=False) #, linecolor='white', linewidths=1)

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=num_iterations, repeat=False)

    savefile = r"test5.gif"
    pillowwriter = animation.PillowWriter(fps=10)
    anim.save(savefile, writer=pillowwriter)

    # plt.show()

if __name__ == '__main__':
    # main()
    # animation_example()
    animation_example_2_mod()