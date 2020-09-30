%global packname  mrMLM.GUI
%global packver   4.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Locus Random-SNP-Effect Mixed Linear Model Tools for Genome-Wide Association Study with Graphical User Interface

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-mrMLM 
BuildRequires:    R-CRAN-sbl 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-lars 
Requires:         R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-mrMLM 
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
