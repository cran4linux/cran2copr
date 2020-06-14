%global packname  abbyyR
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          2%{?dist}
Summary:          Access to Abbyy Optical Character Recognition (OCR) API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-progress 

%description
Get text from images of text using Abbyy Cloud Optical Character
Recognition (OCR) API. Easily OCR images, barcodes, forms, documents with
machine readable zones, e.g. passports. Get the results in a variety of
formats including plain text and XML. To learn more about the Abbyy OCR
API, see <http://ocrsdk.com/>.

%prep
%setup -q -c -n %{packname}


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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
