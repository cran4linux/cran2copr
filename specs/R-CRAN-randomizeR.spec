%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  randomizeR
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Randomization for Clinical Trials

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mstate 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-PwrGSD 
BuildRequires:    R-CRAN-gsDesign 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mstate 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-PwrGSD 
Requires:         R-CRAN-gsDesign 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-reshape2 

%description
This tool enables the user to choose a randomization procedure based on
sound scientific criteria. It comprises the generation of randomization
sequences as well the assessment of randomization procedures based on
carefully selected criteria. Furthermore, 'randomizeR' provides a function
for the comparison of randomization procedures.

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
