%global __brp_check_rpaths %{nil}
%global packname  pdfsearch
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Search Tools for PDF Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-stringi 

%description
Includes functions for keyword search of pdf files. There is also a
wrapper that includes searching of all files within a single directory.

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
%doc %{rlibdir}/%{packname}/joss
%doc %{rlibdir}/%{packname}/pdf
%doc %{rlibdir}/%{packname}/shiny_example
%{rlibdir}/%{packname}/INDEX
