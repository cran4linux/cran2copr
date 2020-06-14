%global packname  bs4Dash
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          2%{?dist}
Summary:          A 'Bootstrap 4' Version of 'shinydashboard'

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-htmltools 

%description
Make 'Bootstrap 4' dashboards. Use the full power of 'AdminLTE3', a
dashboard template built on top of 'Bootstrap 4'
<https://github.com/ColorlibHQ/AdminLTE>.

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
%doc %{rlibdir}/%{packname}/AdminLTE3-3.0.0
%doc %{rlibdir}/%{packname}/bootstrap-4.3.1
%doc %{rlibdir}/%{packname}/bs4Dash-0.2.0
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/jquery-ui-1.12.1
%doc %{rlibdir}/%{packname}/README.md
%doc %{rlibdir}/%{packname}/UI_tests
%{rlibdir}/%{packname}/INDEX
