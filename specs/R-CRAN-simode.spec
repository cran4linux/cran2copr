%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simode
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference for Systems of Ordinary Differential Equations using Separable Integral-Matching

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ncvreg 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ncvreg 

%description
Implements statistical inference for systems of ordinary differential
equations, that uses the integral-matching criterion and takes advantage
of the separability of parameters, in order to obtain initial parameter
estimates for nonlinear least squares optimization. Dattner & Yaari (2018)
<arXiv:1807.04202>. Dattner et al. (2017) <doi:10.1098/rsif.2016.0525>.
Dattner & Klaassen (2015) <doi:10.1214/15-EJS1053>.

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
