%global __brp_check_rpaths %{nil}
%global packname  cropDemand
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Crop Water Demand for Brazil

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-dplyr >= 0.3.0.1
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ncdf4 
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-dplyr >= 0.3.0.1
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ncdf4 

%description
Estimation of crop water demand can be processed via this package. As
example, the data from 'TerraClimate' dataset
(<http://www.climatologylab.org/terraclimate.html>) calibrated with
automatic weather stations of National Meteorological Institute of Brazil
is available in a coarse spatial resolution to do the crop water demand.
However, the user have also the option to download the variables directly
from 'TerraClimate' repository with the download.terraclimate function and
access the original 'TerraClimate' products. If the user believes that is
necessary calibrate the variables, there is another function to do it.
Lastly, the estimation of the crop water demand present in this package
can be run for all the Brazilian territory with 'TerraClimate' dataset.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
