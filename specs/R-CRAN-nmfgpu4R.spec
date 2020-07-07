%global packname  nmfgpu4R
%global packver   0.2.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5.2
Release:          3%{?dist}
Summary:          Non-Negative Matrix Factorization (NMF) using CUDA

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-Matrix 
Requires:         R-CRAN-SparseM 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-utils 

%description
Wrapper package for the nmfgpu library, which implements several
Non-negative Matrix Factorization (NMF) algorithms for CUDA platforms. By
using the acceleration of GPGPU computing, the NMF can be used for
real-world problems inside the R environment. All CUDA devices starting
with Kepler architecture are supported by the library.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
