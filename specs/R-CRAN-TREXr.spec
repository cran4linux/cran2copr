%global __brp_check_rpaths %{nil}
%global packname  TREXr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tree Sap Flow Extractor

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-solaR 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sensitivity 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-tools 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-solaR 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-lubridate 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sensitivity 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-msm 
Requires:         R-parallel 
Requires:         R-CRAN-magrittr 
Requires:         R-tools 

%description
Performs data assimilation, processing and analyses on sap flow data
obtained with the thermal dissipation method (TDM). The package includes
functions for gap filling time-series data, detecting outliers,
calculating data-processing uncertainties and generating uniform data
output and visualisation. The package is designed to deal with large
quantities of data and to apply commonly used data-processing methods. The
functions have been validated on data collected from different tree
species across the northern hemisphere (Peters et al. 2018
<doi:10.1111/nph.15241>).

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
