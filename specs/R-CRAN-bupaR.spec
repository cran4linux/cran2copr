%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bupaR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Business Process Analysis in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.2.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-eventdataR >= 0.2.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-cli >= 3.2.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-eventdataR >= 0.2.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-ggplot2 

%description
Comprehensive Business Process Analysis toolkit. Creates S3-class for
event log objects, and related handler functions. Imports related packages
for filtering event data, computation of descriptive statistics, handling
of 'Petri Net' objects and visualization of process maps. See also
packages 'edeaR','processmapR', 'eventdataR' and 'processmonitR'.

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
