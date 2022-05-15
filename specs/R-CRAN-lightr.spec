%global __brp_check_rpaths %{nil}
%global packname  lightr
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read Spectrometric Data and Metadata

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 

%description
Parse various reflectance/transmittance/absorbance spectra file formats to
extract spectral data and metadata, as described in Gruson, White & Maia
(2019) <doi:10.21105/joss.01857>. Among other formats, it can import files
from 'Avantes' <https://www.avantes.com/>, 'CRAIC'
<https://www.microspectra.com/>, and 'OceanInsight' (formerly
'OceanOptics') <https://www.oceaninsight.com/> brands.

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
