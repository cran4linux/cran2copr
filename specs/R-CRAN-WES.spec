%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WES
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Analyzing Wastewater and Environmental Sampling Data

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.1
Requires:         R-core >= 4.1.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-openmeteo 
BuildRequires:    R-CRAN-chirps 
BuildRequires:    R-CRAN-whitebox 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-CRAN-elevatr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rworldmap 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-openmeteo 
Requires:         R-CRAN-chirps 
Requires:         R-CRAN-whitebox 
Requires:         R-CRAN-exactextractr 
Requires:         R-CRAN-elevatr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rworldmap 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 

%description
Provides reproducible functions for collating and analyzing data from
environmental sampling studies. Environmental Sampling (ES) of infectious
diseases involves collecting samples from various sources (such as sewage,
water, air, soil, or surfaces) to monitor the presence of pathogens in the
environment. Analysis of ES data often requires the calculation of
Real-Time Quantitative PCR (qPCR) variables, normalizing ES observations,
and analyzing sampling site characteristics. To help reduce the complexity
of these analyses we have implemented tools that assist with establishing
standardized ES data formats, absolute and relative quantification of qPCR
data, estimation of qPCR amplification efficiency, and collating
open-source spatial data for sampling sites.

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
