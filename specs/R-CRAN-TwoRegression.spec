%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TwoRegression
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Develop and Apply Two-Regression Algorithms

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-pROC >= 1.16.0
BuildRequires:    R-CRAN-PAutilities >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-pROC >= 1.16.0
Requires:         R-CRAN-PAutilities >= 1.1.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-RcppRoll 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tidyr 

%description
Facilitates development and application of two-regression algorithms for
research-grade wearable devices. It provides an easy way for users to
access previously-developed algorithms, and also to develop their own.
Initial motivation came from Hibbing PR, LaMunion SR, Kaplan AS, & Crouter
SE (2018) <doi:10.1249/MSS.0000000000001532>. However, other algorithms
are now supported. Please see the associated references in the package
documentation for full details of the algorithms that are supported.

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
