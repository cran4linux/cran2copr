%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  varbvs
%global packver   2.6-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.10
Release:          1%{?dist}%{?buildtag}
Summary:          Large-Scale Bayesian Variable Selection Using Variational Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-nor1mix 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-nor1mix 

%description
Fast algorithms for fitting Bayesian variable selection models and
computing Bayes factors, in which the outcome (or response variable) is
modeled using a linear regression or a logistic regression. The algorithms
are based on the variational approximations described in "Scalable
variational inference for Bayesian variable selection in regression, and
its accuracy in genetic association studies" (P. Carbonetto & M. Stephens,
2012, <DOI:10.1214/12-BA703>). This software has been applied to large
data sets with over a million variables and thousands of samples.

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
