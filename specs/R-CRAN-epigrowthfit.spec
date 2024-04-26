%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epigrowthfit
%global packver   0.15.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15.2
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Mixed Effects Models of Epidemic Growth

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-Matrix >= 1.6.2
BuildRequires:    R-CRAN-RcppEigen >= 0.3.4.0.0
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-Matrix >= 1.6.2
Requires:         R-CRAN-TMB 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Maximum likelihood estimation of nonlinear mixed effects models of
epidemic growth using Template Model Builder ('TMB').  Enables joint
estimation for collections of disease incidence time series, including
time series that describe multiple epidemic waves. Supports a set of
widely used phenomenological models: exponential, logistic, Richards
(generalized logistic), subexponential, and Gompertz.  Provides methods
for interrogating model objects and several auxiliary functions, including
one for computing basic reproduction numbers from fitted values of the
initial exponential growth rate. Preliminary versions of this software
were applied in Ma et al. (2014) <doi:10.1007/s11538-013-9918-2> and in
Earn et al. (2020) <doi:10.1073/pnas.2004904117>.

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
