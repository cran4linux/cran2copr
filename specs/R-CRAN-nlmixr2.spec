%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlmixr2
%global packver   4.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Mixed Effects Models in Population PK/PD

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nlmixr2est >= 2.2.2
BuildRequires:    R-CRAN-rxode2 >= 2.1.3
BuildRequires:    R-CRAN-nlmixr2plot >= 2.0.8
BuildRequires:    R-CRAN-nlmixr2extra >= 2.0.10
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-cli >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-lotri >= 0.4.3
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-nlmixr2est >= 2.2.2
Requires:         R-CRAN-rxode2 >= 2.1.3
Requires:         R-CRAN-nlmixr2plot >= 2.0.8
Requires:         R-CRAN-nlmixr2extra >= 2.0.10
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-cli >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-lotri >= 0.4.3
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 

%description
Fit and compare nonlinear mixed-effects models in differential equations
with flexible dosing information commonly seen in pharmacokinetics and
pharmacodynamics (Almquist, Leander, and Jirstrand 2015
<doi:10.1007/s10928-015-9409-1>). Differential equation solving is by
compiled C code provided in the 'rxode2' package (Wang, Hallow, and James
2015 <doi:10.1002/psp4.12052>).

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
