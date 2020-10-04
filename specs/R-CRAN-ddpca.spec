%global packname  ddpca
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
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
Efficient procedures for fitting the DD-PCA (Ke et al., 2019,
<arXiv:1906.00051>) by decomposing a large covariance matrix into a
low-rank matrix plus a diagonally dominant matrix. The implementation of
DD-PCA includes the convex approach using the Alternating Direction Method
of Multipliers (ADMM) and the non-convex approach using the iterative
projection algorithm. Applications of DD-PCA to large covariance matrix
estimation and global multiple testing are also included in this package.

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
