%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  milorGWAS
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed Logistic Regression for Genome-Wide Analysis Studies (GWAS)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gaston >= 1.6
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-gaston >= 1.6
Requires:         R-CRAN-Rcpp >= 1.0.2

%description
Fast approximate methods for mixed logistic regression in genome-wide
analysis studies (GWAS). Two computationnally efficient methods are
proposed for obtaining effect size estimates (beta) in Mixed Logistic
Regression in GWAS: the Approximate Maximum Likelihood Estimate (AMLE),
and the Offset method. The wald test obtained with AMLE is identical to
the score test. Data can be genotype matrices in plink format, or dosage
(VCF files). The methods are described in details in Milet et al (2020)
<doi:10.1101/2020.01.17.910109>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
