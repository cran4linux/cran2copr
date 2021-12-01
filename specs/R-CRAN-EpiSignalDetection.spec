%global __brp_check_rpaths %{nil}
%global packname  EpiSignalDetection
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Signal Detection Analysis

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ISOweek 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-surveillance 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-ISOweek 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-surveillance 
Requires:         R-utils 

%description
Exploring time series for signal detection. It is specifically designed to
detect possible outbreaks using infectious disease surveillance data at
the European Union / European Economic Area or country level. Automatic
detection tools used are presented in the paper "Monitoring count time
series in R: aberration detection in public health surveillance", by
Salmon (2016) <doi:10.18637/jss.v070.i10>. The package includes: - Signal
Detection tool, an interactive 'shiny' application in which the user can
import external data and perform basic signal detection analyses; - An
automated report in HTML format, presenting the results of the time series
analysis in tables and graphs. This report can also be stratified by
population characteristics (see 'Population' variable). This project was
funded by the European Centre for Disease Prevention and Control.

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
