%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mpower
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analysis via Monte Carlo Simulation for Correlated Data

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-sbgcop 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-magrittr 
Requires:         R-parallel 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-sbgcop 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 

%description
A flexible framework for power analysis using Monte Carlo simulation for
settings in which considerations of the correlations between predictors
are important. Users can set up a data generative model that preserves
dependence structures among predictors given existing data (continuous,
binary, or ordinal). Users can also generate power curves to assess the
trade-offs between sample size, effect size, and power of a design. This
package includes several statistical models common in environmental
mixtures studies. For more details and tutorials, see Nguyen et al. (2022)
<arXiv:2209.08036>.

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
