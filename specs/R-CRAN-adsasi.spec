%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adsasi
%global packver   0.9.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Sample Size Simulator

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-abind 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
A simulations-first sample size determination package that aims at making
sample size formulae obsolete for most easily computable statistical
experiments ; the main envisioned use case is clinical trials. The
proposed clinical trial must be written by the user in the form of a
function that takes as argument a sample size and returns a boolean (for
whether or not the trial is a success). The 'adsasi' functions will then
use it to find the correct sample size empirically. The unavoidable
mis-specification is obviated by trying sample size values close to the
right value, the latter being understood as the value that gives the
probability of success the user wants (usually 80 or 90%% in biostatistics,
corresponding to 20 or 10%% type II error).

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
