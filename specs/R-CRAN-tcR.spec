%global packname  tcR
%global packver   2.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.4
Release:          1%{?dist}
Summary:          Advanced Data Analysis of Immune Receptor Repertoires

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-utils >= 3.1.0
BuildRequires:    R-grid >= 3.0.0
BuildRequires:    R-CRAN-data.table >= 1.9.0
BuildRequires:    R-CRAN-reshape2 >= 1.2.0
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-gridExtra >= 0.9
BuildRequires:    R-CRAN-stringdist >= 0.7.3
BuildRequires:    R-CRAN-igraph >= 0.7.1
BuildRequires:    R-CRAN-dplyr >= 0.4.0
BuildRequires:    R-CRAN-scales >= 0.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-gtable >= 0.1.2
Requires:         R-utils >= 3.1.0
Requires:         R-grid >= 3.0.0
Requires:         R-CRAN-data.table >= 1.9.0
Requires:         R-CRAN-reshape2 >= 1.2.0
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-gridExtra >= 0.9
Requires:         R-CRAN-stringdist >= 0.7.3
Requires:         R-CRAN-igraph >= 0.7.1
Requires:         R-CRAN-dplyr >= 0.4.0
Requires:         R-CRAN-scales >= 0.3.0
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-gtable >= 0.1.2

%description
Platform for the advanced analysis of T cell receptor and Immunoglobulin
repertoires data and visualisation of the analysis results.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/crossanalysis.report.Rmd
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/library.report.Rmd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
