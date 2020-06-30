%global packname  lightr
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
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
<http://www.microspectra.com/>, and 'OceanInsight' (formerly
'OceanOptics') <https://www.oceaninsight.com/> brands.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
