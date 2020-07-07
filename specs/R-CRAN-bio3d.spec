%global packname  bio3d
%global packver   2.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.1
Release:          3%{?dist}
Summary:          Biological Structure Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-grid 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 
Requires:         R-grid 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Utilities to process, organize and explore protein structure, sequence and
dynamics data. Features include the ability to read and write structure,
sequence and dynamic trajectory data, perform sequence and structure
database searches, data summaries, atom selection, alignment,
superposition, rigid core identification, clustering, torsion analysis,
distance matrix analysis, structure and sequence conservation analysis,
normal mode analysis, principal component analysis of heterogeneous
structure data, and correlation network analysis from normal mode and
molecular dynamics data. In addition, various utility functions are
provided to enable the statistical and graphical power of the R
environment to work with biological sequence and structural data. Please
refer to the URLs below for more information.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/matrices
%doc %{rlibdir}/%{packname}/staticdocs
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
