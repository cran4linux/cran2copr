%global packname  bnstruct
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          3%{?dist}
Summary:          Bayesian Network Structure Learning from Data with MissingValues

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
Requires:         R-CRAN-bitops 
Requires:         R-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-methods 

%description
Bayesian Network Structure Learning from Data with Missing Values. The
package implements the Silander-Myllymaki complete search, the Max-Min
Parents-and-Children, the Hill-Climbing, the Max-Min Hill-climbing
heuristic searches, and the Structural Expectation-Maximization algorithm.
Available scoring functions are BDeu, AIC, BIC. The package also
implements methods for generating and using bootstrap samples, imputed
data, inference.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
