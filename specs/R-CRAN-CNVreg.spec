%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CNVreg
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          CNV-Profile Regression for Copy Number Variants Association Analysis with Penalized Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-tidyr 

%description
Performs copy number variants association analysis with Lasso and Weighted
Fusion penalized regression. Creates a "CNV profile curve" to represent an
individual’s CNV events across a genomic region so to capture variations
in CNV length and dosage. When evaluating association, the CNV profile
curve is directly used as a predictor in the regression model, avoiding
the need to predefine CNV loci. CNV profile regression estimates CNV
effects at each genome position, making the results comparable across
different studies. The penalization encourages sparsity in variable
selection with a Lasso penalty and encourages effect smoothness between
consecutive CNV events with a weighted fusion penalty, where the weight
controls the level of smoothing between adjacent CNVs. For more details,
see Si (2024) <doi:10.1101/2024.11.23.624994>.

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
