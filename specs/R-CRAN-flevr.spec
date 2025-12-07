%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flevr
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible, Ensemble-Based Variable Selection with Potentially Missing Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ranger 

%description
Perform variable selection in settings with possibly missing data based on
extrinsic (algorithm-specific) and intrinsic (population-level) variable
importance. Uses a Super Learner ensemble to estimate the underlying
prediction functions that give rise to estimates of variable importance.
For more information about the methods, please see Williamson and Huang
(2024) <doi:10.1515/ijb-2023-0059>.

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
