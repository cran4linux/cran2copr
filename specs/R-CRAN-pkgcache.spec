%global packname  pkgcache
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Cache 'CRAN'-Like Metadata and R Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-processx >= 3.3.0.9001
BuildRequires:    R-CRAN-curl >= 3.2
BuildRequires:    R-CRAN-callr >= 2.0.4.9000
BuildRequires:    R-CRAN-cli >= 2.0.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-filelock 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-processx >= 3.3.0.9001
Requires:         R-CRAN-curl >= 3.2
Requires:         R-CRAN-callr >= 2.0.4.9000
Requires:         R-CRAN-cli >= 2.0.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-filelock 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-uuid 

%description
Metadata and package cache for CRAN-like repositories. This is a utility
package to be used by package management tools that want to take advantage
of caching.

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
