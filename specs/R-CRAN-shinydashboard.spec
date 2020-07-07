%global packname  shinydashboard
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          3%{?dist}
Summary:          Create Dashboards with 'Shiny'

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.0.0
BuildRequires:    R-CRAN-htmltools >= 0.2.6
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-promises 
Requires:         R-CRAN-shiny >= 1.0.0
Requires:         R-CRAN-htmltools >= 0.2.6
Requires:         R-utils 
Requires:         R-CRAN-promises 

%description
Create dashboards with 'Shiny'. This package provides a theme on top of
'Shiny', making it easy to create attractive dashboards.

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
%doc %{rlibdir}/%{packname}/AdminLTE
%doc %{rlibdir}/%{packname}/shinydashboard.css
%doc %{rlibdir}/%{packname}/shinydashboard.js
%doc %{rlibdir}/%{packname}/shinydashboard.js.map
%doc %{rlibdir}/%{packname}/shinydashboard.min.js
%doc %{rlibdir}/%{packname}/shinydashboard.min.js.map
%{rlibdir}/%{packname}/INDEX
