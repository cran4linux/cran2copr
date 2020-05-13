%global packname  vroom
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Read and Write Rectangular Text Data Quickly

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-progress >= 1.2.1
BuildRequires:    R-CRAN-rlang >= 0.4.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.18.3
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-rlang >= 0.4.2
Requires:         R-CRAN-Rcpp >= 0.12.18.3
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-lifecycle 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-withr 

%description
The goal of 'vroom' is to read and write data (like 'csv', 'tsv' and
'fwf') quickly. When reading it uses a quick initial indexing step, then
reads the values lazily , so only the data you actually use needs to be
read.  The writer formats the data in parallel and writes to disk
asynchronously from formatting.

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
%doc %{rlibdir}/%{packname}/bench
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%doc %{rlibdir}/%{packname}/words
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
