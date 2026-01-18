%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lavDiag
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Variable Models Diagnostics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-corrplot >= 0.90
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-corrplot >= 0.90
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-withr 

%description
Diagnostics and visualization tools for latent variable models fitted with
'lavaan' (Rosseel, 2012 <doi:10.18637/jss.v048.i02>). The package provides
fast, parallel-safe factor-score prediction (lavPredict_parallel()), data
augmentation with model predictions, residuals, delta-method standard
errors and confidence intervals (augment()), and model-based latent grids
for continuous, ordinal, or mixed indicators (prepare()). It offers
item-level empirical versus model curve comparison using generalized
additive models for both continuous and ordinal indicators (item_data(),
item_plot()) via 'mgcv' (Wood, 2017, ISBN:9781498728331), residual
diagnostics including residual correlation tables and plots (resid_cor(),
resid_corrplot()) using 'corrplot' (Wei and Simko, 2021
<https://github.com/taiyun/corrplot>), and Q–Q checks of residual
z-statistics (resid_qq()), optionally with non-overlapping labels from
'ggrepel' (Slowikowski, 2024
<https://CRAN.R-project.org/package=ggrepel>). Heavy computations are
parallelized via 'future'/'furrr' (Bengtsson, 2021
<doi:10.32614/RJ-2021-048>; Vaughan and Dancho, 2018
<https://CRAN.R-project.org/package=furrr>). Methods build on established
literature and packages listed above.

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
