%global packname  RRphylo
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}
Summary:          Phylogenetic Ridge Regression Methods for Comparative Studies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-pvclust 
BuildRequires:    R-CRAN-mvMORPH 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-binr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-penalized 
BuildRequires:    R-CRAN-smatr 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-outliers 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-tseries 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-geiger 
Requires:         R-stats4 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-pvclust 
Requires:         R-CRAN-mvMORPH 
Requires:         R-CRAN-lmtest 
Requires:         R-parallel 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-binr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-nlme 
Requires:         R-CRAN-penalized 
Requires:         R-CRAN-smatr 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-car 
Requires:         R-CRAN-outliers 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-plotrix 
Requires:         R-cluster 
Requires:         R-CRAN-tseries 

%description
Functions for phylogenetic analysis (Castiglione et al, 2017
<doi:10.1111/2041-210X.12954>). The functions perform the estimation of
phenotypic evolutionary rates, identification of phenotypic evolutionary
rate shifts, quantification of direction and size of evolutionary change
in multivariate traits, and the computation of ontogenetic shape vectors.

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
%{rlibdir}/%{packname}/INDEX
