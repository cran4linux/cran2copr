%global packname  mongolite
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          3%{?dist}
Summary:          Fast and Simple 'MongoDB' Client for R

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    openssl-devel
BuildRequires:    cyrus-sasl-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-jsonlite >= 1.4
BuildRequires:    R-CRAN-openssl >= 1.0
BuildRequires:    R-CRAN-mime 
Requires:         R-CRAN-jsonlite >= 1.4
Requires:         R-CRAN-openssl >= 1.0
Requires:         R-CRAN-mime 

%description
High-performance MongoDB client based on 'mongo-c-driver' and 'jsonlite'.
Includes support for aggregation, indexing, map-reduce, streaming,
encryption, enterprise authentication, and GridFS. The online user manual
provides an overview of the available methods in the package:
<https://jeroen.github.io/mongolite/>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
