%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  collinear
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Multicollinearity Management

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-recipes >= 1.0.9
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-recipes >= 1.0.9
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-rlang 

%description
Provides a comprehensive and automated workflow for managing
multicollinearity in data frames with numeric and/or categorical
variables. The package integrates five robust methods into a single
function: (1) target encoding of categorical variables based on response
values (Micci-Barreca, 2001 (Micci-Barreca, D. 2001
<doi:10.1145/507533.507538>); (2) automated feature prioritization to
preserve key predictors during filtering; (3 and 4) pairwise correlation
and VIF filtering across all variable types (numeric–numeric,
numeric–categorical, and categorical–categorical); (5) adaptive
correlation and VIF thresholds. Together, these methods enable a reliable
multicollinearity management in most use cases while maintaining model
integrity. The package also supports parallel processing and progress
tracking via the packages 'future' and 'progressr', and provides seamless
integration with the 'tidymodels' ecosystem through a dedicated recipe
step.

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
