%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rQSAR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          QSAR Modeling with Multiple Algorithms: MLR, PLS, and Random Forest

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rcdk >= 3.8.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-stats 
Requires:         R-CRAN-rcdk >= 3.8.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-gridExtra 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-leaps 
Requires:         R-stats 

%description
Quantitative Structure-Activity Relationship (QSAR) modeling is a valuable
tool in computational chemistry and drug design, where it aims to predict
the activity or property of chemical compounds based on their molecular
structure. In this vignette, we present the 'rQSAR' package, which
provides functions for variable selection and QSAR modeling using Multiple
Linear Regression (MLR), Partial Least Squares (PLS), and Random Forest
algorithms.

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
