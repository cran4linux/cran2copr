%global packname  TestDesign
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Optimal Test Design Approach to Fixed and Adaptive TestConstruction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-logitnorm 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-logitnorm 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-crayon 

%description
Use the optimal test design approach by Birnbaum (1968,
ISBN:9781593119348) and van der Linden (2018) <doi:10.1201/9781315117430>
in constructing fixed and adaptive tests. Supports the following
mixed-integer programming (MIP) solver packages: 'lpsymphony',
'Rsymphony', 'gurobi', 'lpSolve', and 'Rglpk'. The 'gurobi' package is not
available from CRAN; see <https://www.gurobi.com/downloads>. See vignette
for installing 'Rsymphony' package on Mac systems.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
