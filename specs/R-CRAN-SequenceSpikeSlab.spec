%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SequenceSpikeSlab
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Exact Bayesian Model Selection Methods for the Sparse Normal Sequence Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-selectiveInference >= 1.2.5
BuildRequires:    R-CRAN-RcppProgress >= 0.4.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-selectiveInference >= 1.2.5
Requires:         R-CRAN-RcppProgress >= 0.4.1
Requires:         R-CRAN-Rcpp >= 0.12.18

%description
Contains fast functions to calculate the exact Bayes posterior for the
Sparse Normal Sequence Model, implementing the algorithms described in Van
Erven and Szabo (2021, <doi:10.1214/20-BA1227>). For general hierarchical
priors, sample sizes up to 10,000 are feasible within half an hour on a
standard laptop. For beta-binomial spike-and-slab priors, a faster
algorithm is provided, which can handle sample sizes of 100,000 in half an
hour. In the implementation, special care has been taken to assure
numerical stability of the methods even for such large sample sizes.

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
