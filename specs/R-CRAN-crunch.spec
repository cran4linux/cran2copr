%global packname  crunch
%global packver   1.26.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.26.3
Release:          2%{?dist}
Summary:          Crunch.io Data Tools

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.15
BuildRequires:    R-CRAN-httpcache >= 0.1.4
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9.15
Requires:         R-CRAN-httpcache >= 0.1.4
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-curl 
Requires:         R-grDevices 
Requires:         R-methods 

%description
The Crunch.io service <http://crunch.io/> provides a cloud-based data
store and analytic engine, as well as an intuitive web interface. Using
this package, analysts can interact with and manipulate Crunch datasets
from within R. Importantly, this allows technical researchers to
collaborate naturally with team members, managers, and clients who prefer
a point-and-click interface.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/app.crunch.io
%doc %{rlibdir}/%{packname}/crunch-test.R
%doc %{rlibdir}/%{packname}/cubes
%doc %{rlibdir}/%{packname}/cubes.tgz
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/example-datasets
%doc %{rlibdir}/%{packname}/httptest
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
