%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mighty.component
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mighty Components for ADaM Generation

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 2.5.0
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-xmlparsedata 
BuildRequires:    R-CRAN-zephyr 
Requires:         R-CRAN-withr >= 2.5.0
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-xmlparsedata 
Requires:         R-CRAN-zephyr 

%description
Reusable code templates (components) for the 'mighty' framework, used to
generate Analysis Data Model (ADaM) programs. Components are 'Mustache'
templates documented with 'roxygen2'-like tags. They can be retrieved from
local directories, 'GitHub' or URLs, rendered with study-specific
parameters, validated, evaluated, and unit tested with code coverage.

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
