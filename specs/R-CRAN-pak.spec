%global packname  pak
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Another Approach to Package Installation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-processx >= 3.2.1
BuildRequires:    R-CRAN-curl >= 3.2
BuildRequires:    R-CRAN-callr >= 3.0.0.9002
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-rprojroot >= 1.3.2
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-ps >= 1.3.0
BuildRequires:    R-CRAN-desc >= 1.2.0
BuildRequires:    R-CRAN-pkgcache >= 1.0.3
BuildRequires:    R-CRAN-filelock >= 1.0.2
BuildRequires:    R-CRAN-pkgbuild >= 1.0.2
BuildRequires:    R-CRAN-cli >= 1.0.0
BuildRequires:    R-CRAN-cliapp >= 0.0.0.9002
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rematch2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-processx >= 3.2.1
Requires:         R-CRAN-curl >= 3.2
Requires:         R-CRAN-callr >= 3.0.0.9002
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-rprojroot >= 1.3.2
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-ps >= 1.3.0
Requires:         R-CRAN-desc >= 1.2.0
Requires:         R-CRAN-pkgcache >= 1.0.3
Requires:         R-CRAN-filelock >= 1.0.2
Requires:         R-CRAN-pkgbuild >= 1.0.2
Requires:         R-CRAN-cli >= 1.0.0
Requires:         R-CRAN-cliapp >= 0.0.0.9002
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rematch2 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
The goal of 'pak' is to make package installation faster and more
reliable. In particular, it performs all HTTP operations in parallel, so
metadata resolution and package downloads are fast. Metadata and package
files are cached on the local disk as well. 'pak' has a dependency solver,
so it finds version conflicts before performing the installation. This
version of 'pak' supports CRAN, 'Bioconductor' and 'GitHub' packages as
well.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/tools
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
