%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RSurveillance
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Design and Analysis of Disease Surveillance Activities

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-CRAN-epiR 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mc2d 
Requires:         R-CRAN-epitools 
Requires:         R-CRAN-epiR 
Requires:         R-stats 
Requires:         R-CRAN-mc2d 

%description
A range of functions for the design and analysis of disease surveillance
activities. These functions were originally developed for animal health
surveillance activities but can be equally applied to aquatic animal,
wildlife, plant and human health surveillance activities. Utilities are
included for sample size calculation and analysis of representative
surveys for disease freedom, risk-based studies for disease freedom and
for prevalence estimation. This package is based on Cameron A., Conraths
F., Frohlich A., Schauer B., Schulz K., Sergeant E., Sonnenburg J.,
Staubach C. (2015). R package of functions for risk-based surveillance.
Deliverable 6.24, WP 6 - Decision making tools for implementing risk-based
surveillance, Grant Number no. 310806, RISKSUR
(<https://www.fp7-risksur.eu/sites/default/files/documents/Deliverables/RISKSUR_%%28310806%%29_D6.24.pdf>).
Many of the 'RSurveillance' functions are incorporated into the 'epitools'
website: Sergeant, ESG, 2019. Epitools epidemiological calculators. Ausvet
Pty Ltd. Available at: <http://epitools.ausvet.com.au>.

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
