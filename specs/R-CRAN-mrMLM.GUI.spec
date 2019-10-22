%global packname  mrMLM.GUI
%global packver   3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2
Release:          1%{?dist}
Summary:          Multi-Locus Random-SNP-Effect Mixed Linear Model Tools forGenome-Wide Association Study

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-qqman 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-mrMLM 
Requires:         R-CRAN-shiny 
Requires:         R-MASS 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-qqman 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-mrMLM 

%description
Conduct multi-locus genome-wide association study under the framework of
random-SNP-effect mixed linear model (mrMLM). First, each marker on the
genome is scanned. Bonferroni correction is replaced by a less stringent
selection criterion for significant test. Then, all the markers that are
potentially associated with the trait are included in a multi-locus model,
their effects are estimated by empirical Bayes and true Quantitative Trait
Nucleotides (QTN) are identified by likelihood ratio test. Wen YJ, Zhang
H, Ni YL, Huang B, Zhang J, Feng JY, Wang SB, Dunwell JM, Zhang YM, Wu R
(2018) <doi:10.1093/bib/bbw145>.

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
