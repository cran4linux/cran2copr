%global packname  semantic.dashboard
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Dashboard with Semantic UI Support for 'shiny'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 0.12.1
BuildRequires:    R-CRAN-shiny.semantic >= 0.1.2
BuildRequires:    R-utils 
Requires:         R-CRAN-shiny >= 0.12.1
Requires:         R-CRAN-shiny.semantic >= 0.1.2
Requires:         R-utils 

%description
Basic functions for creating semantic UI dashboard. This package adds
support for a powerful UI library semantic UI - <http://semantic-ui.com/>
to your dashboard and enables you to stay compatible with 'shinydashboard'
functionalities.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/compare.png
%doc %{rlibdir}/%{packname}/prepare_package_cran.sh
%doc %{rlibdir}/%{packname}/themes.png
%{rlibdir}/%{packname}/INDEX
