%global packname  filling
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Matrix Completion, Imputation, and Inpainting Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-ROptSpace 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-ROptSpace 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-nabor 
Requires:         R-utils 

%description
Filling in the missing entries of a partially observed data is one of
fundamental problems in various disciplines of mathematical science. For
many cases, data at our interests have canonical form of matrix in that
the problem is posed upon a matrix with missing values to fill in the
entries under preset assumptions and models. We provide a collection of
methods from multiple disciplines under Matrix Completion, Imputation, and
Inpainting. See Davenport and Romberg (2016)
<doi:10.1109/JSTSP.2016.2539100> for an overview of the topic.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
