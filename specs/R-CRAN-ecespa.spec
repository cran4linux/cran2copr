%global packname  ecespa
%global packver   1.1-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Spatial Point Pattern Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.core 
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.core 

%description
Some wrappers, functions and data sets for for spatial point pattern
analysis (mainly based on 'spatstat'), used in the book "Introduccion al
Analisis Espacial de Datos en Ecologia y Ciencias Ambientales: Metodos y
Aplicaciones" and in the papers by De la Cruz et al. (2008)
<doi:10.1111/j.0906-7590.2008.05299.x> and Olano et al. (2009)
<doi:10.1051/forest:2008074>.

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
