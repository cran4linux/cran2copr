%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  letsR
%global packver   6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Handling and Analysis in Macroecology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 1.0.11
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-geosphere 
Requires:         R-CRAN-sf >= 1.0.11
Requires:         R-CRAN-terra 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-geosphere 

%description
Tools for handling, processing, and analyzing species geographic
distributions, environmental data, and biodiversity patterns across
geographical, environmental, and attribute spaces. Includes functions for
constructing and analyzing species distributions, estimating geographic
ranges from occurrence records, and conducting spatial analyses in
macroecology. See Vilela and Villalobos (2015)
<doi:10.1111/2041-210X.12401> and Vilela et al. (2026)
<doi:10.1111/2041-210X.70421> for details.

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
