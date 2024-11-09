%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  collinear
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Multicollinearity Management

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-ranger 

%description
Effortless multicollinearity management in data frames with both numeric
and categorical variables for statistical and machine learning
applications. The package simplifies multicollinearity analysis by
combining four robust methods: 1) target encoding for categorical
variables (Micci-Barreca, D. 2001 <doi:10.1145/507533.507538>); 2)
automated feature prioritization to prevent key variable loss during
filtering; 3) pairwise correlation for all variable combinations
(numeric-numeric, numeric-categorical, categorical-categorical); and 4)
fast computation of variance inflation factors.

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
