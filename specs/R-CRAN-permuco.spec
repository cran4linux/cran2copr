%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  permuco
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Permutation Tests for Regression, (Repeated Measures) ANOVA/ANCOVA and Comparison of Signals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 

%description
Functions to compute p-values based on permutation tests. Regression,
ANOVA and ANCOVA, omnibus F-tests, marginal unilateral and bilateral
t-tests are available. Several methods to handle nuisance variables are
implemented (Kherad-Pajouh, S., & Renaud, O. (2010)
<doi:10.1016/j.csda.2010.02.015> ; Kherad-Pajouh, S., & Renaud, O. (2014)
<doi:10.1007/s00362-014-0617-3> ; Winkler, A. M., Ridgway, G. R., Webster,
M. A., Smith, S. M., & Nichols, T. E. (2014)
<doi:10.1016/j.neuroimage.2014.01.060>). An extension for the comparison
of signals issued from experimental conditions (e.g. EEG/ERP signals) is
provided. Several corrections for multiple testing are possible, including
the cluster-mass statistic (Maris, E., & Oostenveld, R. (2007)
<doi:10.1016/j.jneumeth.2007.03.024>) and the threshold-free cluster
enhancement (Smith, S. M., & Nichols, T. E. (2009)
<doi:10.1016/j.neuroimage.2008.03.061>).

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
