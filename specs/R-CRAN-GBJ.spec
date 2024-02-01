%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GBJ
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Berk-Jones Test for Set-Based Inference in Genetic Association Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-SKAT 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-SKAT 
Requires:         R-stats 
Requires:         R-CRAN-BH 

%description
Offers the Generalized Berk-Jones (GBJ) test for set-based inference in
genetic association studies. The GBJ is designed as an alternative to
tests such as Berk-Jones (BJ), Higher Criticism (HC), Generalized Higher
Criticism (GHC), Minimum p-value (minP), and Sequence Kernel Association
Test (SKAT). All of these other methods (except for SKAT) are also
implemented in this package, and we additionally provide an omnibus test
(OMNI) which integrates information from each of the tests. The GBJ has
been shown to outperform other tests in genetic association studies when
signals are correlated and moderately sparse. Please see the vignette for
a quickstart guide or Sun and Lin (2017) <arXiv:1710.02469> for more
details.

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
