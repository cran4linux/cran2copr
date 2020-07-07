%global packname  mrMLM
%global packver   4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0
Release:          3%{?dist}
Summary:          Multi-Locus Random-SNP-Effect Mixed Linear Model Tools forGenome-Wide Association Study

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-qqman 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-sbl 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-qqman 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-sbl 

%description
Conduct multi-locus genome-wide association study under the framework of
multi-locus random-SNP-effect mixed linear model (mrMLM). First, each
marker on the genome is scanned. Bonferroni correction is replaced by a
less stringent selection criterion for significant test. Then, all the
markers that are potentially associated with the trait are included in a
multi-locus genetic model, their effects are estimated by empirical Bayes
and all the nonzero effects were further identified by likelihood ratio
test for true QTL. Wen YJ, Zhang H, Ni YL, Huang B, Zhang J, Feng JY, Wang
SB, Dunwell JM, Zhang YM, Wu R (2018) <doi:10.1093/bib/bbw145>.

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
