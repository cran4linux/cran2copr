%global packname  DWBmodelUN
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Water Balance a Hydrological Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 

%description
A tool to hydrologic modelling using the Budyko framework and the Dynamic
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
