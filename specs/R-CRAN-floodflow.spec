%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  floodflow
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Map-First Climate-Informed Flood Assessment for Data-Scarce Basins

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
A reproducible, map-oriented workflow for flood hazard assessment that
chains rainfall extreme value analysis, rainfall-runoff simulation,
terrain-based flow routing and water-depth estimation into a single
pipeline. A stationary-versus-nonstationary test for changing rainfall
extremes is built in, and any flood scenario can be produced for a
present-day or a climate-adjusted design event. Defaults target settings
with sparse gauge networks, using satellite or reanalysis rainfall,
temperature-based potential evapotranspiration and regional pooling of
short records. Heavy modelling engines are wrapped rather than
reimplemented so that the core stays lightweight. Methods follow
established hydrology, including the generalized extreme value
distribution for rainfall maxima (Coles, 2001,
<doi:10.1007/978-1-4471-3675-0>) and Manning's equation for open-channel
flow.

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
