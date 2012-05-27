BUILD_DIR = bin
SRC_DIR = src

SL_SOURCES := $(wildcard $(SRC_DIR)/*.sl)
SLO_TARGETS:= $(SL_SOURCES:.sl=.slo)
SLO_TARGETS:= $(subst src,bin,$(SLO_TARGETS))

SDL_TARGETS:= $(SL_SOURCES:.sl=.sdl)
SDL_TARGETS:= $(subst src,bin,$(SDL_TARGETS))

all: $(SLO_TARGETS) $(SDL_TARGETS) render

$(BUILD_DIR)/%.slo: $(SRC_DIR)/%.sl
	shader -C -o $@ $<

$(BUILD_DIR)/%.sdl: $(SRC_DIR)/%.sl
	shaderdl -o $@ $<

render:
	render rib/grid.rib
