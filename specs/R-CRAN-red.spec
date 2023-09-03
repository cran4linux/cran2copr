%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  red
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          IUCN Redlisting Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BAT 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-predicts 
Requires:         R-CRAN-BAT 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-geosphere 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-predicts 

%description
Includes algorithms to facilitate the assessment of extinction risk of
species according to the IUCN (International Union for Conservation of
Nature, see <https://www.iucn.org/> for more information) red list
criteria.

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
