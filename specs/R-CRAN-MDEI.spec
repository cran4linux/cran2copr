%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MDEI
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Implementing the Method of Direct Estimation and Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-splines2 

%description
Causal and statistical inference on an arbitrary treatment effect curve
requires care in both estimation and inference.  This package, implements
the Method of Direct Estimation and Inference as introduced in "Estimation
and Inference on Nonlinear and Heterogeneous Effects" by Ratkovic and
Tingley (2023) <doi:10.1086/723811>.  The method takes an outcome,
variable of theoretical interest (treatment), and set of variables and
then returns a partial derivative (marginal effect) of the treatment
variable at each point along with uncertainty intervals. The approach
offers two advances. First, a split-sample approach is used as a guard
against over-fitting. Second, the method uses a data-driven interval
derived from conformal inference, rather than relying on a normality
assumption on the error terms.

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
