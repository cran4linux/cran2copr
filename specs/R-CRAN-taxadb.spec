%global packname  taxadb
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          A High-Performance Local Taxonomic Database Interface

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-arkdb 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-arkdb 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-progress 
Requires:         R-utils 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 

%description
Creates a local database of many commonly used taxonomic authorities and
provides functions that can quickly query this data.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
