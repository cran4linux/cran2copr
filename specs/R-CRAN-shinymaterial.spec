%global packname  shinymaterial
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          1%{?dist}
Summary:          Implement Material Design in Shiny Applications

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 0.7.0
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-shiny >= 0.7.0
Requires:         R-CRAN-jsonlite 

%description
Allows shiny developers to incorporate UI elements based on Google's
Material design. See <https://material.io/guidelines/> for more
information.

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
%doc %{rlibdir}/%{packname}/css
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/icons
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/js
%doc %{rlibdir}/%{packname}/materialize
%{rlibdir}/%{packname}/INDEX
