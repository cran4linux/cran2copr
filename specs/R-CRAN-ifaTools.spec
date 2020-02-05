%global packname  ifaTools
%global packver   0.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.21
Release:          1%{?dist}
Summary:          Toolkit for Item Factor Analysis with 'OpenMx'

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-OpenMx >= 2.3.1
BuildRequires:    R-CRAN-rpf >= 0.48
BuildRequires:    R-CRAN-shiny >= 0.10
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-methods 
Requires:         R-CRAN-OpenMx >= 2.3.1
Requires:         R-CRAN-rpf >= 0.48
Requires:         R-CRAN-shiny >= 0.10
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-methods 

%description
Tools, tutorials, and demos of Item Factor Analysis using 'OpenMx'.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example
%doc %{rlibdir}/%{packname}/itemModelExplorer
%doc %{rlibdir}/%{packname}/modelBuilder
%{rlibdir}/%{packname}/INDEX
