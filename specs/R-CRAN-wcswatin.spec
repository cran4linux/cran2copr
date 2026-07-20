%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wcswatin
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Weather and Climate Inputs for 'SWAT'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-hyfo 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-hyfo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 
Requires:         R-methods 

%description
Provides workflows to prepare weather and climate time series from gridded
and station data for 'SWAT' ('Soil and Water Assessment Tool'). Supports
data extraction, aggregation, interpolation, quality control, unit
conversion, and export of per-location model input files. For the
underlying model, see Arnold et al. (1998) "Large Area Hydrologic Modeling
and Assessment Part I: Model Development"
<doi:10.1111/j.1752-1688.1998.tb05961.x>.

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
