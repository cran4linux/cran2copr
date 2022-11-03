%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcmdrPlugin.EACSPIR
%global packver   0.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Plugin de R-Commander para el Manual 'EACSPIR'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.8.0
BuildRequires:    R-CRAN-R2HTML 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-ez 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-RcmdrMisc 
Requires:         R-CRAN-Rcmdr >= 2.8.0
Requires:         R-CRAN-R2HTML 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-ez 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-RcmdrMisc 

%description
Este paquete proporciona una interfaz grafica de usuario (GUI) para
algunos de los procedimientos estadisticos detallados en un curso de
'Estadistica aplicada a las Ciencias Sociales mediante el programa
informatico R' (EACSPIR). LA GUI se ha desarrollado como un Plugin del
programa R-Commander.

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
