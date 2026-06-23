%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nocturn
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Sleep Data Filtering and Visualisation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-edfReader 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rsvg 
BuildRequires:    R-CRAN-svgedit 
BuildRequires:    R-CRAN-qpdf 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-edfReader 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rsvg 
Requires:         R-CRAN-svgedit 
Requires:         R-CRAN-qpdf 

%description
An online app and command-line utility to import, filter and visualise
sleep data. Can be used with sleep data collected from any type of device
(e.g. radar, sleep diary,...) as long as the data contains sleep onset and
wake-up times for each sleep session.

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
