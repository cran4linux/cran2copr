%global packname  rerf
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}
Summary:          Randomer Forest

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppZiggurat 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dummies 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-parallel 
Requires:         R-CRAN-RcppZiggurat 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-dummies 
Requires:         R-CRAN-mclust 

%description
R-RerF (aka Randomer Forest (RerF) or Random Projection Forests) is an
algorithm developed by Tomita (2016) <arXiv:1506.03410v2> which is similar
to Random Forest - Random Combination (Forest-RC) developed by Breiman
(2001) <doi:10.1023/A:1010933404324>.  Random Forests create
axis-parallel, or orthogonal trees. That is, the feature space is
recursively split along directions parallel to the axes of the feature
space. Thus, in cases in which the classes seem inseparable along any
single dimension, Random Forests may be suboptimal.  To address this,
Breiman also proposed and characterized Forest-RC, which uses linear
combinations of coordinates rather than individual coordinates, to split
along.  This package, 'rerf', implements RerF which is similar to
Forest-RC.  The difference between the two algorithms is where the random
linear combinations occur: Forest-RC combines features at the per tree
level whereas RerF takes linear combinations of coordinates at every node
in the tree.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
