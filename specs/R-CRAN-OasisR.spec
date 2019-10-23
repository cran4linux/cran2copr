%global packname  OasisR
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}
Summary:          Outright Tool for the Analysis of Spatial Inequalities andSegregation

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.6.0
BuildRequires:    R-CRAN-rgdal >= 1.4.3
BuildRequires:    R-CRAN-measurements >= 1.3.0
BuildRequires:    R-CRAN-spdep >= 1.1.2
BuildRequires:    R-CRAN-seg >= 0.5.5
BuildRequires:    R-CRAN-rgeos >= 0.4.3
BuildRequires:    R-CRAN-outliers >= 0.14
Requires:         R-methods >= 3.6.0
Requires:         R-CRAN-rgdal >= 1.4.3
Requires:         R-CRAN-measurements >= 1.3.0
Requires:         R-CRAN-spdep >= 1.1.2
Requires:         R-CRAN-seg >= 0.5.5
Requires:         R-CRAN-rgeos >= 0.4.3
Requires:         R-CRAN-outliers >= 0.14

%description
A set of indexes and tests for the analysis of social segregation.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
