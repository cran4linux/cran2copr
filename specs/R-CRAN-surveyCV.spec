%global __brp_check_rpaths %{nil}
%global packname  surveyCV
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cross Validation Based on Survey Design

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survey >= 4.1
BuildRequires:    R-CRAN-magrittr >= 2.0
Requires:         R-CRAN-survey >= 4.1
Requires:         R-CRAN-magrittr >= 2.0

%description
Functions to generate K-fold cross validation (CV) folds and CV test error
estimates that take into account how a survey dataset's sampling design
was constructed (SRS, clustering, stratification, and/or unequal sampling
weights). You can input linear and logistic regression models, along with
data and a type of survey design in order to get an output that can help
you determine which model best fits the data using K-fold cross
validation. Our paper on "K-Fold Cross-Validation for Complex Sample
Surveys" by Wieczorek, Guerin, and McMahon (2022) <doi:10.1002/sta4.454>
explains why differing how we take folds based on survey design is useful.

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
