%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmdisc
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Discretization and Grouping for Logistic Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppNumerical 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-gam 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-RcppNumerical 
Requires:         R-stats 

%description
A Stochastic-Expectation-Maximization (SEM) algorithm (Celeux et al.
(1995) <https://inria.hal.science/inria-00074164>) associated with a Gibbs
sampler which purpose is to learn a constrained representation for
logistic regression that is called quantization (Ehrhardt et al. (2019)
<doi:10.48550/arXiv.1903.08920>). Continuous features are discretized and
categorical features' values are grouped to produce a better logistic
regression model. Pairwise interactions between the discretized and
grouped features are dynamically added to the model through a
Metropolis-Hastings algorithm (Hastings, W. K. (1970)
<doi:10.1093/biomet/57.1.97>).

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
