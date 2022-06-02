%global __brp_check_rpaths %{nil}
%global packname  LUCIDus
%global packver   2.1.5-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Unknown Clustering with Integrated Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mix 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mix 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-progress 

%description
An implementation of LUCID model (Peng (2019)
<doi:10.1093/bioinformatics/btz667>). LUCID conducts integrated clustering
using exposures, omics data (and outcome of interest). An EM algorithm is
implemented to estimate MLE of LUCID model. LUCID features integrated
variable selection, incorporation of missing omics data, bootstrap
inference and visualization via Sankey diagram.

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
