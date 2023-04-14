%global __brp_check_rpaths %{nil}
%global packname  DWDLargeR
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fast Algorithms for Large Scale Generalized Distance WeightedDiscrimination

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-SparseM 
Requires:         R-methods 
Requires:         R-stats 

%description
Solving large scale distance weighted discrimination. The main algorithm
is a symmetric Gauss-Seidel based alternating direction method of
multipliers (ADMM) method. See Lam, X.Y., Marron, J.S., Sun, D.F., and
Toh, K.C. (2018) <arXiv:1604.05473> for more details.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
