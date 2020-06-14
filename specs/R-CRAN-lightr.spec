%global packname  lightr
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
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
'OceanOptics') <https://www.oceaninsight.com/> brands. This package has
been peer-reviewed by rOpenSci (v. 0.1).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/lightr.bib
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/testdata_sources.txt
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
