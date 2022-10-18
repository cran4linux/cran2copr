%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CMMs
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compositional Mediation Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-robCompositions 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-robCompositions 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-dplyr 

%description
A compositional mediation model for continuous outcome and binary outcomes
to deal with mediators that are compositional data. Lin, Ziqiang et al.
(2022) <doi:10.1016/j.jad.2021.12.019>.

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
