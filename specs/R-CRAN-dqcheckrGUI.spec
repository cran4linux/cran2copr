%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dqcheckrGUI
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Point-and-Click GUI Client for 'dqcheckr'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dqcheckr >= 0.2.2
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-shinyvalidate 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
Requires:         R-CRAN-dqcheckr >= 0.2.2
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-shinyvalidate 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-stats 
Requires:         R-tools 

%description
A graphical user interface for the 'dqcheckr' package. Provides a
point-and-click 'shiny' application for configuring dataset quality
checks, running them against recurring file deliveries, and browsing
historical check results — without writing any R code.

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
