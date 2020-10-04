%global packname  gqlr
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          'GraphQL' Server in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-graphql >= 1.3
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-graphql >= 1.3
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-jsonlite 

%description
Server implementation of 'GraphQL'
<http://graphql.github.io/graphql-spec/>, a query language originally
created by Facebook for describing data requirements on complex
application data models.  Visit <http://graphql.org> to learn more about
'GraphQL'.

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
%{rlibdir}/%{packname}/INDEX
