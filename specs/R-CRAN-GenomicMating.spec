%global packname  GenomicMating
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Efficient Breeding by Genomic Mating

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-emoa 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-SOMbrero 
BuildRequires:    R-CRAN-kohonen 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-LowRankQP 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-emoa 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-SOMbrero 
Requires:         R-CRAN-kohonen 
Requires:         R-CRAN-plotly 
Requires:         R-graphics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-LowRankQP 

%description
Implements the genomic mating approach in the recently published article:
Akdemir, D., & Sanchez, J. I. (2016). Efficient Breeding by Genomic
Mating. Frontiers in Genetics, 7. <DOI:10.3389/fgene.2016.00210>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
