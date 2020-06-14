%global packname  semantic.dashboard
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          2%{?dist}
Summary:          Dashboard with Semantic UI Support for Shiny

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 0.12.1
BuildRequires:    R-CRAN-shiny.semantic >= 0.1.2
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-shiny >= 0.12.1
Requires:         R-CRAN-shiny.semantic >= 0.1.2
Requires:         R-utils 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-glue 

%description
It offers functions for creating dashboard with Semantic UI.

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
%doc %{rlibdir}/%{packname}/compare.png
%doc %{rlibdir}/%{packname}/semantic.dashboard.js
%doc %{rlibdir}/%{packname}/semantic.dashboard.min.js
%doc %{rlibdir}/%{packname}/themes.png
%{rlibdir}/%{packname}/INDEX
