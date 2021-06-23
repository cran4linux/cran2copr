%global __brp_check_rpaths %{nil}
%global packname  spatsoc
%global packver   0.1.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.16
Release:          1%{?dist}%{?buildtag}
Summary:          Group Animal Relocation Data by Spatial and Temporal Relationship

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    geos-devel >= 3.2.0
BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.10.5
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-adehabitatHR 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table >= 1.10.5
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-adehabitatHR 
Requires:         R-CRAN-igraph 
Requires:         R-methods 

%description
Detects spatial and temporal groups in GPS relocations (Robitaille et al.
(2020) <doi:10.1111/2041-210X.13215>). It can be used to convert GPS
relocations to gambit-of-the-group format to build proximity-based social
networks In addition, the randomizations function provides data-stream
randomization methods suitable for GPS data.

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
