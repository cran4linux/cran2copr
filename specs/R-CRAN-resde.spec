%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  resde
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation in Reducible Stochastic Differential Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-nlme 
Requires:         R-methods 

%description
Maximum likelihood estimation for univariate reducible stochastic
differential equation models. Discrete, possibly noisy observations, not
necessarily evenly spaced in time. Can fit multiple individuals/units with
global and local parameters, by fixed-effects or mixed-effects methods.
Ref.: Garcia, O. (2019) "Estimating reducible stochastic differential
equations by conversion to a least-squares problem", Computational
Statistics 34(1): 23-46, <doi:10.1007/s00180-018-0837-4>.

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
