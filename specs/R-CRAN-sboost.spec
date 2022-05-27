%global __brp_check_rpaths %{nil}
%global packname  sboost
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning with AdaBoost on Decision Stumps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-stats >= 3.4
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-rlang >= 0.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
Requires:         R-stats >= 3.4
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-rlang >= 0.2.1
Requires:         R-CRAN-Rcpp >= 0.12.17

%description
Creates classifier for binary outcomes using Adaptive Boosting (AdaBoost)
algorithm on decision stumps with a fast C++ implementation. For a
description of AdaBoost, see Freund and Schapire (1997)
<doi:10.1006/jcss.1997.1504>. This type of classifier is nonlinear, but
easy to interpret and visualize. Feature vectors may be a combination of
continuous (numeric) and categorical (string, factor) elements. Methods
for classifier assessment, predictions, and cross-validation also
included.

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
