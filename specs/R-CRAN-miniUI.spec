%global __brp_check_rpaths %{nil}
%global packname  miniUI
%global packver   0.1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Shiny UI Widgets for Small Screens

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools >= 0.3
BuildRequires:    R-CRAN-shiny >= 0.13
BuildRequires:    R-utils 
Requires:         R-CRAN-htmltools >= 0.3
Requires:         R-CRAN-shiny >= 0.13
Requires:         R-utils 

%description
Provides UI widget and layout functions for writing Shiny apps that work
well on small screens.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
