%global packname  ddpca
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Diagonally Dominant Principal Component Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-MASS 
Requires:         R-CRAN-RSpectra 
Requires:         R-Matrix 
Requires:         R-CRAN-quantreg 
Requires:         R-MASS 

%description
Consider the problem of decomposing a large covariance matrix into a low
rank matrix plus a diagonally dominant matrix. This problem is called
Diagonally Dominant Principal Component Analysis (DD-PCA) in the reference
Ke, Z., Xue, L. and Yang, F. (2019) <arXiv:1906.00051>. DD-PCA can be used
in covariance matrix estimation and global detection in multiple testing.
This package implements DD-PCA using both convex approach and non-convex
approach; Convex approach refers to solving a convex relaxation of the
original problem using Alternating Direction Method of Multipliers (ADMM),
while non-convex approach resorts to an iterative projection algorithm.
This package also implements two global testing methods proposed in the
reference.

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
%{rlibdir}/%{packname}/INDEX
