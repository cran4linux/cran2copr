%global packname  philentropy
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}
Summary:          Similarity and Distance Quantification Between ProbabilityFunctions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-KernSmooth 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-dplyr 
Requires:         R-KernSmooth 

%description
Computes 46 optimized distance and similarity measures for comparing
probability functions (Drost (2018) <doi:10.21105/joss.00765>). These
comparisons between probability functions have their foundations in a
broad range of scientific disciplines from mathematics to ecology. The aim
of this package is to provide a core framework for clustering,
classification, statistical inference, goodness-of-fit, non-parametric
statistics, information theory, and machine learning tasks that are based
on comparing univariate or multivariate probability functions.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
