%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LUCIDus
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          LUCID with Multiple Omics Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-glmnet 

%description
Implements Latent Unknown Clusters By Integrating Multi-omics Data (LUCID;
Peng (2019) <doi:10.1093/bioinformatics/btz667>) for integrative
clustering with exposures, multi-omics data, and health outcomes. Supports
three integration strategies: early, parallel, and serial. Provides model
fitting and tuning, lasso-type regularization for exposure and omics
feature selection, handling of missing data, including both sporadic and
complete-case patterns, prediction, and g-computation for estimating
causal effects of exposures, bootstrap inference for uncertainty
estimation, and S3 summary and plot methods. For the multi-omics
integration framework, see Jia (2024)
<https://journal.r-project.org/articles/RJ-2024-012/RJ-2024-012.pdf>. For
the missing-data imputation mechanism, see Jia (2024)
<doi:10.1093/bioadv/vbae123>.

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
