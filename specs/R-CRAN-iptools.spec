%global __brp_check_rpaths %{nil}
%global packname  iptools
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          3%{?dist}%{?buildtag}
Summary:          Manipulate, Validate and Resolve 'IP' Addresses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-AsioHeaders 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-triebeard 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-AsioHeaders 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-triebeard 

%description
A toolkit for manipulating, validating and testing 'IP' addresses and
ranges, along with datasets relating to 'IP' addresses. Tools are also
provided to map 'IPv4' blocks to country codes. While it primarily has
support for the 'IPv4' address space, more extensive 'IPv6' support is
intended.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/test
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
