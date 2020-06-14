%global packname  ghql
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          General Purpose 'GraphQL' Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-graphql 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-graphql 

%description
A 'GraphQL' client, with an R6 interface for initializing a connection to
a 'GraphQL' instance, and methods for constructing queries, including
fragments and parameterized queries. Queries are checked with the
'libgraphqlparser' C++ parser via the 'gaphql' package.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ignore
%doc %{rlibdir}/%{packname}/js
%{rlibdir}/%{packname}/INDEX
