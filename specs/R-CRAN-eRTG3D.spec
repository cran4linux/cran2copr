%global __brp_check_rpaths %{nil}
%global packname  eRTG3D
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Empirically Informed Random Trajectory Generation in 3-D

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-raster >= 2.9.5
BuildRequires:    R-CRAN-pbapply >= 1.4.1
BuildRequires:    R-CRAN-rasterVis >= 0.45
BuildRequires:    R-CRAN-CircStats >= 0.2.6
BuildRequires:    R-CRAN-tiff >= 0.1.5
Requires:         R-CRAN-plotly >= 4.9.0
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-raster >= 2.9.5
Requires:         R-CRAN-pbapply >= 1.4.1
Requires:         R-CRAN-rasterVis >= 0.45
Requires:         R-CRAN-CircStats >= 0.2.6
Requires:         R-CRAN-tiff >= 0.1.5

%description
Creates realistic random trajectories in a 3-D space between two given fix
points, so-called conditional empirical random walks (CERWs). The
trajectory generation is based on empirical distribution functions
extracted from observed trajectories (training data) and thus reflects the
geometrical movement characteristics of the mover. A digital elevation
model (DEM), representing the Earth's surface, and a background layer of
probabilities (e.g. food sources, uplift potential, waterbodies, etc.) can
be used to influence the trajectories. Unterfinger M (2018). "3-D
Trajectory Simulation in Movement Ecology: Conditional Empirical Random
Walk". Master's thesis, University of Zurich.
<https://www.geo.uzh.ch/dam/jcr:6194e41e-055c-4635-9807-53c5a54a3be7/MasterThesis_Unterfinger_2018.pdf>.
Technitis G, Weibel R, Kranstauber B, Safi K (2016). "An algorithm for
empirically informed random trajectory generation between two endpoints".
GIScience 2016: Ninth International Conference on Geographic Information
Science, 9, online. <doi:10.5167/uzh-130652>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
