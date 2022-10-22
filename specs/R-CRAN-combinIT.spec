%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  combinIT
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Combined Interaction Test for Unreplicated Two-Way Tables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-mvtnorm 

%description
There are several non-functional-form-based interaction tests for testing
interaction in unreplicated two-way layouts. However, no single test can
detect all patterns of possible interaction and the tests are sensitive to
a particular pattern of interaction. This package combines six
non-functional-form-based interaction tests for testing additivity. These
six tests were proposed by Boik (1993) <doi:10.1080/02664769300000004>,
Piepho (1994), Kharrati-Kopaei and Sadooghi-Alvandi (2007)
<doi:10.1080/03610920701386851>, Franck et al. (2013)
<doi:10.1016/j.csda.2013.05.002>, Malik et al. (2016)
<doi:10.1080/03610918.2013.870196> and Kharrati-Kopaei and Miller (2016)
<doi:10.1080/00949655.2015.1057821>. The p-values of these six tests are
combined by Bonferroni, Sidak, Jacobi polynomial expansion, and the
Gaussian copula methods to provide researchers with a testing approach
which leverages many existing methods to detect disparate forms of
non-additivity. This package is based on the following published paper:
Shenavari and Kharrati-Kopaei (2018) "A Method for Testing Additivity in
Unreplicated Two-Way Layouts Based on Combining Multiple Interaction
Tests". In addition, several sentences in help files or descriptions were
copied from that paper.

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
