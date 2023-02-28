%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  heteromixgm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Copula Graphical Models for Heterogeneous Mixed Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.10
Requires:         R-core >= 3.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-BDgraph 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-BDgraph 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 

%description
A multi-core R package that allows for the statistical modeling of
multi-group multivariate mixed data using Gaussian graphical models.
Combining the Gaussian copula framework with the fused graphical lasso
penalty, the 'heteromixgm' package can handle a wide variety of datasets
found in various sciences. The package also includes an option to perform
model selection using the AIC, BIC and EBIC information criteria, as well
as simulate mixed heterogeneous data for exploratory or simulation
purposes and one multi-group multivariate mixed agricultural dataset
pertaining to maize yields. The package implements the methodological
developments found in Hermes et al. (2022)
<doi:10.48550/arXiv.2210.13140>.

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
