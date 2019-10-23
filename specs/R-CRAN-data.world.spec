%global packname  data.world
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Functions and Add-Ins for Working with 'data.world' Data Setsand Projects

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dwapi >= 0.1.3
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-ini 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-dwapi >= 0.1.3
Requires:         R-CRAN-httr 
Requires:         R-CRAN-ini 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringi 

%description
High-level tools for working with 'data.world' data sets. 'data.world' is
a platform where you can find interesting data, store and showcase your
own data and data projects, and find and collaborate with other members.
In addition to exploring, querying and charting data on the data.world
site, you can access data via 'API' endpoints and integrations. Use this
package to access, query and explore data sets, and to publish your
insights. Visit <https://data.world>, for additional information.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/dw-bootstrap.css
%doc %{rlibdir}/%{packname}/dw-logo@2x.png
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
