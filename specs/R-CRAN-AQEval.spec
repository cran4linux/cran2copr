%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AQEval
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Air Quality Evaluation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openair 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-loa 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-openair 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-loa 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-segmented 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggtext 
Requires:         R-stats 
Requires:         R-CRAN-data.table 

%description
Developed for use by those tasked with the routine detection,
characterisation and quantification of discrete changes in air quality
time-series, such as identifying the impacts of air quality policy
interventions. The main functions use signal isolation then
break-point/segment (BP/S) methods based on 'strucchange' and 'segmented'
methods to detect and quantify change events (Ropkins & Tate, 2021,
<doi:10.1016/j.scitotenv.2020.142374>).

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
