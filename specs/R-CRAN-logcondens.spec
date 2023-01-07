%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  logcondens
%global packver   2.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate a Log-Concave Probability Density from Iid Observations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-ks 
Requires:         R-graphics 
Requires:         R-stats 

%description
Given independent and identically distributed observations X(1), ...,
X(n), compute the maximum likelihood estimator (MLE) of a density as well
as a smoothed version of it under the assumption that the density is
log-concave, see Rufibach (2007) and Duembgen and Rufibach (2009). The
main function of the package is 'logConDens' that allows computation of
the log-concave MLE and its smoothed version. In addition, we provide
functions to compute (1) the value of the density and distribution
function estimates (MLE and smoothed) at a given point (2) the
characterizing functions of the estimator, (3) to sample from the
estimated distribution, (5) to compute a two-sample permutation test based
on log-concave densities, (6) the ROC curve based on log-concave estimates
within cases and controls, including confidence intervals for given values
of false positive fractions (7) computation of a confidence interval for
the value of the true density at a fixed point. Finally, three datasets
that have been used to illustrate log-concave density estimation are made
available.

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
