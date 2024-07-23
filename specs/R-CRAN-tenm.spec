%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tenm
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Temporal Ecological Niche Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-terra > 1.7.5
BuildRequires:    R-CRAN-rgl > 1.2
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
Requires:         R-CRAN-terra > 1.7.5
Requires:         R-CRAN-rgl > 1.2
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 

%description
Implements methods and functions to calibrate time-specific niche models
(multi-temporal calibration), letting users execute a strict calibration
and selection process of niche models based on ellipsoids, as well as
functions to project the potential distribution in the present and in
global change scenarios.The 'tenm' package has functions to recover
information that may be lost or overlooked while applying a data curation
protocol. This curation involves preserving occurrences that may appear
spatially redundant (occurring in the same pixel) but originate from
different time periods. A novel aspect of this package is that it might
reconstruct the fundamental niche more accurately than mono-calibrated
approaches. The theoretical background of the package can be found in
Peterson et al. (2011)<doi:10.5860/CHOICE.49-6266>.

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
