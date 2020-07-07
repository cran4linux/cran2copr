%global packname  stevedore
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          3%{?dist}
Summary:          Docker Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         docker
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.3
BuildRequires:    R-CRAN-yaml >= 2.1.18
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-curl >= 2.3
Requires:         R-CRAN-yaml >= 2.1.18
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-jsonlite 

%description
Work with containers over the Docker API.  Rather than using system calls
to interact with a docker client, using the API directly means that we can
receive richer information from docker.  The interface in the package is
automatically generated using the 'OpenAPI' (a.k.a., 'swagger')
specification, and all return values are checked in order to make them
type stable.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/images
%doc %{rlibdir}/%{packname}/py
%doc %{rlibdir}/%{packname}/spec
%{rlibdir}/%{packname}/INDEX
