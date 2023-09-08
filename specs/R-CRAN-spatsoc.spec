%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatsoc
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Group Animal Relocation Data by Spatial and Temporal Relationship

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.10.5
BuildRequires:    R-CRAN-adehabitatHR >= 0.4.21
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-data.table >= 1.10.5
Requires:         R-CRAN-adehabitatHR >= 0.4.21
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-units 

%description
Detects spatial and temporal groups in GPS relocations (Robitaille et al.
(2019) <doi:10.1111/2041-210X.13215>).  It can be used to convert GPS
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
