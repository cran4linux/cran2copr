%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ExtremalDep
%global packver   0.0.4-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Extremal Dependence Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-cluster 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-fda 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-cluster 

%description
A set of procedures for parametric and non-parametric modelling of the
dependence structure of multivariate extreme-values is provided. The
statistical inference is performed with non-parametric estimators,
likelihood-based estimators and Bayesian techniques. It adapts the
methodologies of Beranger and Padoan (2015)
<doi:10.48550/arXiv.1508.05561>, Marcon et al. (2016)
<doi:10.1214/16-EJS1162>, Marcon et al. (2017) <doi:10.1002/sta4.145>,
Marcon et al. (2017) <doi:10.1016/j.jspi.2016.10.004> and Beranger et al.
(2021) <doi:10.1007/s10687-019-00364-0>. This package also allows for the
modelling of spatial extremes using flexible max-stable processes. It
provides simulation algorithms and fitting procedures relying on the
Stephenson-Tawn likelihood as per Beranger at al. (2021)
<doi:10.1007/s10687-020-00376-1>.

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
