%global packname  ggsolvencyii
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          A 'ggplot2'-Plot of Composition of Solvency II SCR: SF and IM

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 

%description
An implementation of 'ggplot2'-methods to present the composition of
Solvency II Solvency Capital Requirement (SCR) as a series of concentric
circle-parts. Solvency II (Solvency 2) is European insurance legislation,
coming in force by the delegated acts of October 10, 2014.
<https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL%3A2015%3A012%3ATOC>.
Additional files, defining the structure of the Standard Formula (SF)
method of the SCR-calculation are provided. The structure files can be
adopted for localization or for insurance companies who use Internal
Models (IM). Options are available for combining smaller components,
horizontal and vertical scaling, rotation, and plotting only some
circle-parts. With outlines and connectors several SCR-compositions can be
compared, for example in ORSA-scenarios (Own Risk and Solvency
Assessment).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
