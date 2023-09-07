%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ImML
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Algorithms Fitting and Validation for Forestry

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.94
BuildRequires:    R-CRAN-randomForest >= 4.7.1.1
BuildRequires:    R-CRAN-rpart >= 4.1.19
BuildRequires:    R-stats >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-e1071 >= 1.7.13
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-caret >= 6.0.94
Requires:         R-CRAN-randomForest >= 4.7.1.1
Requires:         R-CRAN-rpart >= 4.1.19
Requires:         R-stats >= 4.1.0
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-e1071 >= 1.7.13
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-rlang >= 1.1.1

%description
Fitting and validation of machine learning algorithms for volume
prediction of trees, currently for conifer trees based on diameter at
breast height and height as explanatory variables.

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
