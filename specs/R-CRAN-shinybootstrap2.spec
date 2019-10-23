%global packname  shinybootstrap2
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Bootstrap 2 Web Components for Use with Shiny

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 0.9
BuildRequires:    R-CRAN-htmltools >= 0.2.6
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-jsonlite >= 0.9
Requires:         R-CRAN-htmltools >= 0.2.6
Requires:         R-CRAN-shiny 

%description
Provides Bootstrap 2 web components for use with the Shiny package. With
versions of Shiny prior to 0.11, these Bootstrap 2 components were
included as part of the package. Later versions of Shiny include Bootstrap
3, so the Bootstrap 2 components have been moved into this package for
those uses who rely on features specific to Bootstrap 2.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
