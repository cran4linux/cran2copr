%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autoslider.core
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Slide Automation for Tables, Listings and Figures

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tern >= 0.9.6
BuildRequires:    R-CRAN-flextable >= 0.9.4
BuildRequires:    R-CRAN-rtables >= 0.6.10
BuildRequires:    R-CRAN-officer >= 0.3.18
BuildRequires:    R-CRAN-rlistings >= 0.2.9
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-tern >= 0.9.6
Requires:         R-CRAN-flextable >= 0.9.4
Requires:         R-CRAN-rtables >= 0.6.10
Requires:         R-CRAN-officer >= 0.3.18
Requires:         R-CRAN-rlistings >= 0.2.9
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-yaml 

%description
The normal process of creating clinical study slides is that a
statistician manually type in the numbers from outputs and a separate
statistician to double check the typed in numbers. This process is time
consuming, resource intensive, and error prone. Automatic slide generation
is a solution to address these issues. It reduces the amount of work and
the required time when creating slides, and reduces the risk of errors
from manually typing or copying numbers from the output to slides. It also
helps users to avoid unnecessary stress when creating large amounts of
slide decks in a short time window.

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
