%global packname  QTL.gCIMapping
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          1%{?dist}
Summary:          QTL Genome-Wide Composite Interval Mapping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-parcor 
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-MASS 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-parcor 

%description
Conduct multiple quantitative trait loci (QTL) mapping under the framework
of random-QTL-effect mixed linear model. First, each position on the
genome is detected in order to construct a negative logarithm P-value
curve against genome position. Then, all the peaks on each effect
(additive or dominant) curve are viewed as potential QTL, all the effects
of the potential QTL are included in a multi-QTL model, their effects are
estimated by empirical Bayes in doubled haploid or by adaptive lasso in
F2, and true QTL are identified by likelihood radio test. Wang S-B, Wen
Y-J, Ren W-L, Ni Y-L, Zhang J, Feng J-Y, Zhang Y-M (2016)
<doi:10.1038/srep29951>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
