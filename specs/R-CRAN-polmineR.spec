%global packname  polmineR
%global packver   0.7.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.11
Release:          1%{?dist}
Summary:          Toolkit for Corpus Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RcppCWB >= 0.2.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-RcppCWB >= 0.2.2
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-slam 
Requires:         R-Matrix 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-stringi 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-knitr 

%description
Library for corpus analysis using the Corpus Workbench as an efficient
back end for indexing and querying large corpora. The package offers
functionality to flexibly create partitions and to carry out basic
statistical operations (count, co-occurrences etc.). The original full
text of documents can be reconstructed and inspected at any time. Beyond
that, the package is intended to serve as an interface to packages
implementing advanced statistical procedures. Respective data structures
(document term matrices, term co- occurrence matrices etc.) can be created
based on the indexed corpora.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
sed -i '/HOME\|INFO/d' %{buildroot}%{rlibdir}/%{packname}/extdata/cwb/registry/*
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/css
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/docker
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/graffle
%doc %{rlibdir}/%{packname}/init
%doc %{rlibdir}/%{packname}/Rscript
%doc %{rlibdir}/%{packname}/sh
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/sticker
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
