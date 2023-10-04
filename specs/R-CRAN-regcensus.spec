%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  regcensus
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Accessing Data from the 'RegCensusAPI'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-dplyr 

%description
Allowing users to access data from the 'RegCensusAPI'. The 'RegCensusAPI'
is an API client that connects to the 'RegData' regulatory restrictions
data by the 'Mercatus Center' at 'George Mason University'. 'RegData' uses
machine learning algorithms to quantify the number of regulatory
restrictions in a jurisdiction. You can find out more about 'RegData' from
'QuantGov website' <https://www.quantgov.org>.

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
