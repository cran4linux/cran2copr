%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pQTLdata
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Proteome Panels and Meta-Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-Rdpack 

%description
It aggregates protein panel data and metadata for protein quantitative
trait locus (pQTL) analysis using 'pQTLtools'
(<https://jinghuazhao.github.io/pQTLtools/>). The package includes data
from affinity-based panels such as 'Olink' (<https://olink.com/>) and
'SomaScan' (<https://somalogic.com/>), as well as mass spectrometry-based
panels from 'CellCarta' (<https://cellcarta.com/>) and 'Seer'
(<https://seer.bio/>). The metadata encompasses updated annotations and
publication details.

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
