%global packname  cranly
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          3%{?dist}
Summary:          Package Directives and Collaboration Networks in CRAN

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-tm 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-tm 

%description
Core visualizations and summaries for the CRAN package database. The
package provides comprehensive methods for cleaning up and organizing the
information in the CRAN package database, for building package directives
networks (depends, imports, suggests, enhances, linking to) and
collaboration networks, producing package dependence trees, and for
computing useful summaries and producing interactive visualizations from
the resulting networks and summaries. The resulting networks can be
coerced to 'igraph' <https://CRAN.R-project.org/package=igraph> objects
for further analyses and modelling.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/art
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
