%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  slideimp
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Numeric Matrices K-NN and PCA Imputation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildRequires:    R-CRAN-mirai >= 2.5.0
BuildRequires:    R-CRAN-dqrng >= 0.4.1
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-mirai >= 2.5.0
Requires:         R-CRAN-dqrng >= 0.4.1
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RhpcBLASctl 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 

%description
Fast k-nearest neighbor (K-NN) and principal component analysis (PCA)
imputation of missing values in high-dimensional numeric matrices, such as
DNA methylation data. PCA imputation can use a locally optimal block
preconditioned conjugate gradient (LOBPCG) eigensolver, which warm-starts
each iteration from the previous eigenblock and search direction.
Group-wise imputation, for example by chromosome, is recommended for
Illumina DNA methylation arrays such as 450K and EPIC, and for other
matrices with groupable columns. Sliding-window imputation imputes columns
ordered by position. Tuning functions choose hyperparameters by masking
observed values, imputing them, and scoring the result over repeated
random masks. The Bayesian PCA sampler draws multiple imputations of the
missing values. For whole-genome methylation data, such as whole-genome
bisulfite sequencing (WGBS) or Enzymatic Methyl-seq (EM-seq), the sampler
is recommended because such data are sparsely observed. The K-NN method is
described in Troyanskaya et al. (2001)
<doi:10.1093/bioinformatics/17.6.520>. PCA imputation is an optimized
reimplementation of imputePCA() from the 'missMDA' package, described in
Josse and Husson (2016) <doi:10.18637/jss.v070.i01>. The sampler
implements the Bayesian method of MIPCA() in 'missMDA', described in
Audigier, Husson and Josse (2016) <doi:10.1080/00949655.2015.1104683>.

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
