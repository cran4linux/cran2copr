%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wflo
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Data Set and Helper Functions for Wind Farm Layout Optimization Problems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-emstreeR 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-emstreeR 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sf 

%description
Provides a convenient data set, a set of helper functions, and a benchmark
function for economically (profit) driven wind farm layout optimization.
This enables researchers in the field of the NP-hard (non-deterministic
polynomial-time hard) problem of wind farm layout optimization to focus on
their optimization methodology contribution and also provides a realistic
benchmark setting for comparability among contributions. See
Croonenbroeck, Carsten & Hennecke, David (2020)
<doi:10.1016/j.energy.2020.119244>.

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
