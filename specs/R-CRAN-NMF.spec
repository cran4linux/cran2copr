%global packname  NMF
%global packver   0.21.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.21.0
Release:          1%{?dist}
Summary:          Algorithms and Framework for Nonnegative Matrix Factorization(NMF)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-rngtools >= 1.2.3
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-pkgmaker >= 0.20
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-registry 
BuildRequires:    R-cluster 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridBase 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-rngtools >= 1.2.3
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-pkgmaker >= 0.20
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-registry 
Requires:         R-cluster 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-digest 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-CRAN-gridBase 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
Provides a framework to perform Non-negative Matrix Factorization (NMF).
The package implements a set of already published algorithms and seeding
methods, and provides a framework to test, develop and plug new/custom
algorithms. Most of the built-in algorithms have been optimized in C++,
and the main interface function provides an easy way of performing
parallel computations on multicore machines.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
