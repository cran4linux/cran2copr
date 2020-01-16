%global packname  igraph
%global packver   1.2.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4.2
Release:          1%{?dist}
Summary:          Network Analysis and Visualization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel
BuildRequires:    libxml2-devel
BuildRequires:    glpk-devel
Requires:         gmp
Requires:         libxml2
Requires:         glpk
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-pkgconfig >= 2.0.0
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-pkgconfig >= 2.0.0
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-utils 

%description
Routines for simple graphs and network analysis. It can handle large
graphs very well and provides functions for generating random and regular
graphs, graph visualization, centrality methods and much more.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/benchmarks
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/html_library.license.terms
%doc %{rlibdir}/%{packname}/html_library.tcl
%doc %{rlibdir}/%{packname}/igraph.gif
%doc %{rlibdir}/%{packname}/igraph2.gif
%doc %{rlibdir}/%{packname}/my_html_library.tcl
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/README.md
%doc %{rlibdir}/%{packname}/tkigraph_help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
