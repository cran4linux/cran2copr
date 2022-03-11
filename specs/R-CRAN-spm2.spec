%global __brp_check_rpaths %{nil}
%global packname  spm2
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Predictive Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-spm 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-psy 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-spm 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-psy 
Requires:         R-CRAN-gbm 
Requires:         R-stats 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-e1071 

%description
An updated and extended version of 'spm' package, by introducing some
further novel functions for modern statistical methods (i.e., generalised
linear models, glmnet, generalised least squares), thin plate splines,
support vector machine, kriging methods (i.e., simple kriging, universal
kriging, block kriging, kriging with an external drift), and novel hybrid
methods (228 hybrids plus numerous variants) of modern statistical methods
or machine learning methods with mathematical and/or univariate
geostatistical methods for spatial predictive modelling. For each method,
two functions are provided, with one function for assessing the predictive
errors and accuracy of the method based on cross-validation, and the other
for generating spatial predictions. It also contains a couple of functions
for data preparation and predictive accuracy assessment.

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
