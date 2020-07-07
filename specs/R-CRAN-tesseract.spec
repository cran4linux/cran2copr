%global packname  tesseract
%global packver   4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1
Release:          3%{?dist}
Summary:          Open Source OCR Engine

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    tesseract-devel >= 3.03
BuildRequires:    leptonica-devel
Requires:         tesseract
Requires:         leptonica
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-pdftools >= 1.5
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-pdftools >= 1.5
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-curl 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-digest 

%description
Bindings to 'Tesseract'
<https://opensource.google.com/projects/tesseract>: a powerful optical
character recognition (OCR) engine that supports over 100 languages. The
engine is highly configurable in order to tune the detection algorithms
and obtain the best possible results.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/COPYRIGHT
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
