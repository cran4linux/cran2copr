%global packname  GermaParl
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          Download and Augment the Corpus of Plenary Protocols of theGerman Bundestag

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cwbtools >= 0.2.0
BuildRequires:    R-CRAN-polmineR 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppCWB 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-RCurl 
Requires:         R-CRAN-cwbtools >= 0.2.0
Requires:         R-CRAN-polmineR 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-RcppCWB 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-RCurl 

%description
Data package to disseminate the 'GermaParl' corpus of parliamentary
debates of the German Bundestag prepared in the 'PolMine Project'. The
package includes a small subset of the corpus for demonstration and
testing purposes. The package includes functionality to load the full
corpus from the open science repository 'Zenodo' and some auxiliary
functions to enhance the corpus.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/sticker
%{rlibdir}/%{packname}/INDEX
