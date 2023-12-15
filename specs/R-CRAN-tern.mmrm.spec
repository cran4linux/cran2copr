%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tern.mmrm
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tables and Graphs for Mixed Models for Repeated Measures (MMRM)

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-emmeans >= 1.6
BuildRequires:    R-CRAN-tern >= 0.9.3
BuildRequires:    R-CRAN-rtables >= 0.6.6
BuildRequires:    R-CRAN-formatters >= 0.5.5
BuildRequires:    R-CRAN-mmrm >= 0.3.5
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-emmeans >= 1.6
Requires:         R-CRAN-tern >= 0.9.3
Requires:         R-CRAN-rtables >= 0.6.6
Requires:         R-CRAN-formatters >= 0.5.5
Requires:         R-CRAN-mmrm >= 0.3.5
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Mixed models for repeated measures (MMRM) are a popular choice for
analyzing longitudinal continuous outcomes in randomized clinical trials
and beyond; see for example Cnaan, Laird and Slasor (1997)
<doi:10.1002/(SICI)1097-0258(19971030)16:20%%3C2349::AID-SIM667%%3E3.0.CO;2-E>.
This package provides an interface for fitting MMRM within the 'tern'
<https://cran.r-project.org/package=tern> framework by Zhu et al. (2023)
and tabulate results easily using 'rtables'
<https://cran.r-project.org/package=rtables> by Becker et al. (2023). It
builds on 'mmrm' <https://cran.r-project.org/package=mmrm> by Sabanés Bové
et al. (2023) for the actual MMRM computations.

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
