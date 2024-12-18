%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  healthatlas
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Explore and Import 'Metopio' Health Atlas Data and Spatial Layers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-chk 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-chk 

%description
Allows for painless use of the 'Metopio' health atlas APIs
<https://metopio.com/how-it-works/atlas/> to explore and import data.
'Metopio' health atlases store open public health data. See what topics
(or indicators) are available among specific populations, periods, and
geographic layers. Download relevant data along with geographic boundaries
or point datasets. Spatial datasets are returned as 'sf' objects.

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
