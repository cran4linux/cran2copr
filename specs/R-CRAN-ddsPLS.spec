%global packname  ddsPLS
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Data-Driven Sparse Partial Least Squares Robust to MissingSamples for Mono and Multi-Block Data Sets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-corrplot 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-RColorBrewer 
Requires:         R-MASS 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-corrplot 

%description
Allows to build Multi-Data-Driven Sparse Partial Least Squares models.
Multi-blocks with high-dimensional settings are particularly sensible to
this. It comes with visualization functions and uses 'Rcpp' functions for
fast computations and 'doParallel' to parallelize cross-validation. This
is based on H Lorenzo, J Saracco, R Thiebaut (2019) <arXiv:1901.04380>.
Many applications have been successfully realized. See
<https://hadrienlorenzo.netlify.com/> for more information, documentation
and examples.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
