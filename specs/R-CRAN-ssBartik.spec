%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ssBartik
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          End-to-End Pipeline for Shift-Share (Bartik) Instrumental Variables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 

%description
Construction, diagnostics, estimation, exposure-robust inference and
publication-ready visualisation for shift-share (Bartik) instrumental
variable designs, in one consistent workflow. Organised around the two
identification routes of the modern literature. The exogenous share
approach refers to Goldsmith-Pinkham, Sorkin and Swift (2020)
<doi:10.1257/aer.20181047> and the exogenous shift approach refers to
Borusyak, Hull and Jaravel (2022) <doi:10.1093/restud/rdab030> and Adao,
Kolesar and Morales (2019) <doi:10.1093/qje/qjz025>. Wraps 'ShiftShareSE'
for exposure-robust inference when available.

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
