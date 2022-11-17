%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MatchIt
%global packver   4.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Preprocessing for Parametric Causal Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-backports >= 1.1.9
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-backports >= 1.1.9
Requires:         R-CRAN-Rcpp 

%description
Selects matched samples of the original treated and control groups with
similar covariate distributions -- can be used to match exactly on
covariates, to match on propensity scores, or perform a variety of other
matching procedures.  The package also implements a series of
recommendations offered in Ho, Imai, King, and Stuart (2007)
<DOI:10.1093/pan/mpl013>. (The 'gurobi' package, which is not on CRAN, is
optional and comes with an installation of the Gurobi Optimizer, available
at <https://www.gurobi.com>.)

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
