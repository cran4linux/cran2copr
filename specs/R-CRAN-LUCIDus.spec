%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LUCIDus
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
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
An implementation of estimating the Latent Unknown Clusters By Integrating
Multi-omics Data (LUCID) model (Peng (2019)
<doi:10.1093/bioinformatics/btz667>). LUCID conducts integrated clustering
using exposures, omics information (and outcome information as an option).
This package implements three different integration strategies for
multi-omics data analysis within the LUCID framework: LUCID early
integration (the original LUCID model), LUCID in parallel (intermediate
integration), and LUCID in serial (late integration). Automated model
selection for each LUCID model is available to obtain the optimal number
of latent clusters, and an integrated imputation approach is implemented
to handle sporadic and list-wise missingness in multi-omics data.
Lasso-type regularity for exposure and omics features were added. S3
methods for summary and plotting functions were fixed.

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
