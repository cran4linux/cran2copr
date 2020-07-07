%global packname  gromovlab
%global packver   0.7-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.6
Release:          3%{?dist}
Summary:          Gromov-Hausdorff Type Distances for Labeled Metric Spaces

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-glpkAPI 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-cluster 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-glpkAPI 
Requires:         R-CRAN-quadprog 
Requires:         R-cluster 
Requires:         R-stats 

%description
Computing Gromov-Hausdorff type l^p distances for labeled metric spaces.
These distances were introduced in V.Liebscher, Gromov meets Phylogenetics
- new Animals for the Zoo of Metrics on Tree Space. preprint
arXiv:1504.05795, for phylogenetic trees but may apply to much more
situations.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
