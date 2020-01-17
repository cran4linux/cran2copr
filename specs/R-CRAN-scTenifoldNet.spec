%global packname  scTenifoldNet
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Construct and Compare scGRN from Single-Cell Transcriptomic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-RSpectra 
Requires:         R-Matrix 
Requires:         R-CRAN-rTensor 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-MASS 

%description
A workflow based on machine learning methods to construct and compare
single-cell gene regulatory networks (scGRN) using single-cell RNA-seq
(scRNA-seq) data collected from different conditions. Uses principal
component regression, tensor decomposition, and manifold alignment, to
accurately identify even subtly shifted gene expression programs.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/python
%{rlibdir}/%{packname}/INDEX
