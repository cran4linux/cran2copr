%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DWBmodelUN
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Water Balance a Hydrological Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-terra 

%description
A tool for hydrologic modelling using the Budyko framework and the Dynamic
Water Balance model with Dynamical Dimension Search algorithm to calibrate
the model and analyze the outputs from interactive graphics. It allows to
calculate the water availability in basins and also some water fluxes
represented by the structure of the model. See Zhang, L., N., Potter, K.,
Hickel, Y., Zhang, Q., Shao (2008) <DOI:10.1016/j.jhydrol.2008.07.021>
"Water balance modeling over variable time scales based on the Budyko
framework - Model development and testing", Journal of Hydrology, 360,
117–131. See Tolson, B., C., Shoemaker (2007) <DOI:10.1029/2005WR004723>
"Dynamically dimensioned search algorithm for computationally efficient
watershed model calibration", Water Resources Research, 43, 1–16.

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
