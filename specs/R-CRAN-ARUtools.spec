%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ARUtools
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Management and Processing of Autonomous Recording Unit (ARU) Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spsurvey >= 5.0.1
BuildRequires:    R-CRAN-seewave >= 2.2.3
BuildRequires:    R-CRAN-fs >= 1.6.1
BuildRequires:    R-CRAN-hms >= 1.1.2
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-lutz 
BuildRequires:    R-CRAN-parzer 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-suncalc 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-spsurvey >= 5.0.1
Requires:         R-CRAN-seewave >= 2.2.3
Requires:         R-CRAN-fs >= 1.6.1
Requires:         R-CRAN-hms >= 1.1.2
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-here 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-lutz 
Requires:         R-CRAN-parzer 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-suncalc 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-units 
Requires:         R-CRAN-withr 

%description
Parse Autonomous Recording Unit (ARU) data and for sub-sampling
recordings. Extract Metadata from your recordings, select a subset of
recordings for interpretation, and prepare files for processing on the
'WildTrax' <https://wildtrax.ca/> platform. Read and process metadata from
recordings collected using the SongMeter and BAR-LT types of ARUs.

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
