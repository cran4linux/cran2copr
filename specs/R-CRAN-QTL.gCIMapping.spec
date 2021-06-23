%global __brp_check_rpaths %{nil}
%global packname  QTL.gCIMapping
%global packver   3.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          QTL Genome-Wide Composite Interval Mapping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-qtl 
Requires:         R-methods 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
Conduct multiple quantitative trait loci (QTL) mapping under the framework
of random-QTL-effect linear mixed model. First, each position on the
genome is detected in order to obtain a negative logarithm P-value curve
against genome position. Then, all the peaks on each effect (additive or
dominant) curve are viewed as potential QTL, all the effects of the
potential QTL are included in a multi-QTL model, their effects are
estimated by empirical Bayes in doubled haploid population or by adaptive
lasso in F2 population, and true QTL are identified by likelihood radio
test. See Wen et al. (2018) <doi:10.1093/bib/bby058>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
