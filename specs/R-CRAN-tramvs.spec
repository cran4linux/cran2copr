%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tramvs
%global packver   0.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Subset Selection for Transformation Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tram >= 0.6.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-variables 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cotram 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-tram >= 0.6.1
Requires:         R-stats 
Requires:         R-CRAN-variables 
Requires:         R-methods 
Requires:         R-CRAN-cotram 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-mvtnorm 

%description
Greedy optimal subset selection for transformation models (Hothorn et al.,
2018, <doi:10.1111/sjos.12291> ) based on the abess algorithm (Zhu et al.,
2020, <doi:10.1073/pnas.2014241117> ). Applicable to models from packages
'tram' and 'cotram'. Application to shift-scale transformation models are
described in Siegfried et al. (2024, <doi:10.1080/00031305.2023.2203177>).

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
