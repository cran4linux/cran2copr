%global packname  getLattes
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Import and Process Data from the 'Lattes' Curriculum Platform

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-pipeR 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-XML 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-pipeR 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 

%description
Tool for import and process data from 'Lattes' curriculum platform
(<http://lattes.cnpq.br/>). The Brazilian government keeps an extensive
base of curricula for academics from all over the country, with over 5
million registrations. The academic life of the Brazilian researcher, or
related to Brazilian universities, is documented in 'Lattes'. Some
information that can be obtained: professional formation, research area,
publications, academics advisories, projects, etc. 'getLattes' package
allows work with 'Lattes' data exported to XML format.

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
%{rlibdir}/%{packname}/INDEX
