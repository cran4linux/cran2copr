%global packname  caret
%global packver   6.0-88
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.88
Release:          1%{?dist}%{?buildtag}
Summary:          Classification and Regression Training

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-withr >= 2.0.0
BuildRequires:    R-CRAN-ModelMetrics >= 1.2.2.2
BuildRequires:    R-CRAN-lattice >= 0.20
BuildRequires:    R-CRAN-recipes >= 0.1.10
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-pROC 
Requires:         R-CRAN-withr >= 2.0.0
Requires:         R-CRAN-ModelMetrics >= 1.2.2.2
Requires:         R-CRAN-lattice >= 0.20
Requires:         R-CRAN-recipes >= 0.1.10
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-pROC 

%description
Misc functions for training and plotting classification and regression
models.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
