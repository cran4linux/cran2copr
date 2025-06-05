%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ordinalsimr
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Compare Ordinal Endpoints Using Simulations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.4
BuildRequires:    R-CRAN-bslib >= 0.9.0
BuildRequires:    R-CRAN-golem >= 0.4.0
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-shiny >= 1.7.4
Requires:         R-CRAN-bslib >= 0.9.0
Requires:         R-CRAN-golem >= 0.4.0
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Simultaneously evaluate multiple ordinal outcome measures. Applied data
analysts in particular are faced with uncertainty in choosing appropriate
statistical tests for ordinal data. The included 'shiny' application
allows users to simulate outcomes given different ordinal data
distributions.

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
