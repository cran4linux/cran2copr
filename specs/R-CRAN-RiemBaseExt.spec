%global packname  RiemBaseExt
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Extension to 'RiemBase' Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RiemBase >= 0.2.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RiemBase >= 0.2.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-cluster 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-kernlab 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-energy 

%description
We provide a number of off-the-shelf algorithms for clustering, elementary
computation, and others. See Bhattacharya and Bhattacharya (2012)
<doi:10.1017/CBO9781139094764> for more details regarding statistics on
manifolds.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
