from landscape_SETUP import *

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- MAIN *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

def plot_wind_figures (windspeed_dataset, total_sand_vol, total_aval_vol, initial_sand_heights_grid, sand_heights_grid, windspeed_grid, w_soil_moisture_grid):
    #Plot windspeed
    plt.figure(0); plt.plot(windspeed_dataset)
    plt.xlabel("Wind iterations"); plt.ylabel("Wind velocity (m/s)"); plt.title("Wind velocity")
    plt.savefig('./windspeed_Timeserie.png')

    #Plot eroded volume
    plt.figure(1); plt.subplot(1,2,1); plt.plot(total_sand_vol)
    plt.plot([0, 0],[0, 1.05],color="white")
    plt.xlabel("Wind iterations"); plt.ylabel("Volume (m^3)"); plt.title("Erosion volume")
    
    #Plot avalanching volume
    plt.subplot(1,2,2); plt.plot(total_aval_vol)
    plt.plot([0, 0],[0, 1.05],color="white")
    plt.xlabel("Wind iterations"); plt.ylabel("Volume (m^3)"); plt.title("Avalanching volume")
    plt.savefig('./ErodAvalVol_fig.png')
    
    #Plot sand heights, initial and final
    plt.figure(2); plt.subplot(1,2,1)
    plt.imshow(initial_sand_heights_grid, cmap='jet', interpolation='none'); plt.title("Initial sand heights"); plt.colorbar()
    plt.subplot(1,2,2)
    plt.imshow(sand_heights_grid, cmap='jet', interpolation='none'); plt.title("Final sand heights"); plt.colorbar()
    plt.savefig('./SandHeight_fig.png')
    
    #Plot final windspeed and moisture
    plt.figure(3); plt.subplot(1,2,1)  
    plt.imshow(windspeed_grid, cmap='jet', interpolation='none'); plt.title("Final windspeed grid"); plt.colorbar()
    plt.subplot(1,2,2)
    plt.imshow(w_soil_moisture_grid, cmap='jet', interpolation='none'); plt.clim(0, 1.0); plt.title("Final moisture grid"); plt.colorbar()    
    plt.savefig('./WindspeedMoist_fig.png')

    # Close all open figures
    plt.close('all')
    
def plot_veg_figures (initial_veg_grid, veg_grid, initial_apparent_veg_type_grid, apparent_veg_type_grid, porosity_grid, age_grid, walls_grid, interaction_field, total_veg_pop, average_age_table, veg_proportions, rainfall_series, exposed_wall_proportions):
    #Plot veg heights, initial and final 
    plt.figure(4); plt.subplot(1,2,1)
    plt.imshow(initial_veg_grid, cmap='jet', interpolation='none'); plt.colorbar(); plt.clim(0, 2.0); plt.title("Initial veg heights") 
    plt.figure(4); plt.subplot(1,2,2)
    plt.imshow(veg_grid, cmap='jet', interpolation='none'); plt.colorbar(); plt.clim(0, 2.0); plt.title("Final veg heights")
    plt.savefig('./VegHeight_fig.png') 
    
    #Plot probability of survival 
    plt.figure(5); plt.subplot(1, 2, 1); plt.imshow(interaction_field, cmap='jet', interpolation='none'); plt.colorbar(); plt.clim(0, 1); plt.title('Neighbourhood stress')
    plt.subplot(1, 2, 2); plt.imshow(age_grid, cmap='summer_r', interpolation='none'); plt.colorbar(); plt.clim(0, 300); plt.title('Plant age')
    plt.savefig('./ProbSurvival_fig.png')

    #Plot vegetation type
    plt.figure(6); plt.subplot(1,2,1)
    plt.imshow(initial_apparent_veg_type_grid, cmap='gnuplot', interpolation='none'); plt.clim(0, 3.); plt.title("Initial veg types"); plt.colorbar()
    plt.subplot(1,2,2)
    plt.imshow(apparent_veg_type_grid, cmap='gnuplot', interpolation='none'); plt.clim(0, 3.); plt.title("Final veg types"); plt.colorbar()
    plt.savefig('./VegType_fig.png')

    #Plot walls grid
    plt.figure(7); plt.imshow(walls_grid, cmap='jet', interpolation='none'); plt.colorbar(); plt.title('Solid walls')
    plt.savefig('./Walls_fig.png')
    
    #Plot population change
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    time = np.arange(0, veg_iterations)
    ax1.plot(time, (total_veg_pop/(Nr*Nc)), 'g-')
    ax2.plot(time, rainfall_series, 'b-')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Population density', color='g')
    ax2.set_ylabel('Precipitation (annual equivalent, mm)', color='b')
    ax1.set_ylim([0, 1])   
    plt.title("Population density and precipitation")
    plt.savefig('./Popdens_Timeserie.png')
    
    #Plot alpha vs population
    fig, ax3 = plt.subplots()
    ax3.plot(rainfall_series, (total_veg_pop/(Nr*Nc))); ax3.invert_xaxis()
    ax3.set_xlabel("Precipitation (annual equivalent, mm)"); ax3.set_ylabel("Population density")
    ax3.set_ylim([0, 1])  
    plt.title("Population density vs precipitation")
    plt.savefig('./PopDensPrecip_fig.png')
    
    #Plot average age
    fig, ax4 = plt.subplots()
    ax4.plot(time, average_age_table[:, 0], 'g-', time, average_age_table[:, 1], 'b-', time, average_age_table[:, 2], 'r-')
    ax4.set_xlabel('Time')
    ax4.set_ylabel('Average plant age', color='k')
    plt.legend(['Grass', 'Shrub', 'Tree'])
    ax4.set_ylim([0, 1000]) 
    plt.title("Average age")
    plt.savefig('./VegAge_Timeserie.png')
    
    #Plot veg type proportions
    fig, ax5 = plt.subplots()
    ax5.plot(time, veg_proportions[:, 0], 'g-', time, veg_proportions[:, 1], 'b-', veg_proportions[:, 2], 'r-')
    ax5.set_xlabel('Time')
    ax5.set_ylabel('Proportion of total veg cover', color='k')
    plt.legend(['Grass', 'Shrub', 'Tree'])
    ax5.set_ylim([0, 1.2])
    plt.title("Plant proportions")
    plt.savefig('./VegProport_TimeSerie.png')
    
    #Plot wall exposures
    plt.figure(); plt.plot(exposed_wall_proportions)
    plt.plot([0, 0],[0, 1.05],color="white")
    plt.xlabel("Model iterations"); plt.ylabel("% of exposed walls"); plt.title("Exposed walls")
    plt.savefig('./WallExpo_fig.png')

    #Close all open figures
    plt.close('all')
  
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
