%global packname  expp
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Analysis of Extra-Pair Paternity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-spatstat.geom 

%description
Tools and data to accompany Schlicht, L., Valcu, M., & Kempenaers, B.
(2015) <doi:10.1111/1365-2656.12293>. Spatial patterns of extra-pair
paternity: beyond paternity gains and losses. Journal of Animal Ecology,
84(2), 518-531.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
