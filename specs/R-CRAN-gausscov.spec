%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gausscov
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          The Gaussian Covariate Method for Variable Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
Requires:         R-stats 

%description
The standard linear regression theory whether frequentist or Bayesian is
based on an 'assumed (revealed?) truth' (John Tukey) attitude to models.
This is reflected in the language of statistical inference which involves
a concept of truth, for example confidence intervals, hypothesis testing
and consistency. The motivation behind this package was to remove the word
true from the theory and practice of linear regression and to replace it
by approximation. The approximations considered are the least squares
approximations. An approximation is called valid if it contains no
irrelevant covariates. This is operationalized using the concept of a
Gaussian P-value which is the probability that pure Gaussian noise is
better in term of least squares than the covariate. The precise definition
given in the paper "An Approximation Based Theory of Linear Regression".
Only four simple equations are required. Moreover the Gaussian P-values
can be simply derived from standard F P-values. Furthermore they are exact
and valid whatever the data in contrast F P-values are only valid for
specially designed simulations. A valid approximation is one where all the
Gaussian P-values are less than a threshold p0 specified by the
statistician, in this package with the default value 0.01. This
approximations approach is not only much simpler it is overwhelmingly
better than the standard model based approach. The will be demonstrated
using high dimensional regression and vector autoregression real data
sets. The goal is to find valid approximations. The search function is
f1st which is a greedy forward selection procedure which results in either
just one or no approximations which may however not be valid. If the size
is less than than a threshold with default value 21 then an all subset
procedure is called which returns the best valid subset. A good default
start is f1st(y,x,kmn=15) The best function for returning multiple
approximations is f3st which repeatedly calls f1st. For more information
see the papers: L. Davies and L. Duembgen, "Covariate Selection Based on a
Model-free Approach to Linear Regression with Exact Probabilities",
<doi:10.48550/arXiv.2202.01553>, L. Davies, "An Approximation Based Theory
of Linear Regression", 2024, <doi:10.48550/arXiv.2402.09858>.

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
