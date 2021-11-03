%global __brp_check_rpaths %{nil}
%global packname  ndtv
%global packver   0.13.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.2
Release:          1%{?dist}%{?buildtag}
Summary:          Network Dynamic Temporal Visualizations

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-animation >= 2.4
BuildRequires:    R-CRAN-network >= 1.13
BuildRequires:    R-CRAN-networkDynamic >= 0.9
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-statnet.common 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-base64 
Requires:         R-CRAN-animation >= 2.4
Requires:         R-CRAN-network >= 1.13
Requires:         R-CRAN-networkDynamic >= 0.9
Requires:         R-CRAN-sna 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-statnet.common 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-base64 

%description
Renders dynamic network data from 'networkDynamic' objects as movies,
interactive animations, or other representations of changing relational
structures and attributes.

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
