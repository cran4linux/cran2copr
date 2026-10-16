%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tabby
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Interfaces for Tabular Deep Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-parsnip >= 1.6.1
BuildRequires:    R-CRAN-dials >= 1.4.4
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-parsnip >= 1.6.1
Requires:         R-CRAN-dials >= 1.4.4
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 

%description
Model definitions for fitting, tuning, and predicting with deep learning
models for tabular data using the 'parsnip' and 'tidymodels' frameworks.
Supported models include the 'TabPFN' foundation model of Hollmann et al.
(2025) <doi:10.1038/s41586-024-08328-6>, 'TabICL' by Qu et al. (2025)
<doi:10.48550/arXiv.2502.05564>, 'SAINT' by Somepalli et al. (2021)
<doi:10.48550/arXiv.2106.01342>, and the tabular 'ResNet' of Gorishniy et
al. (2021) <doi:10.48550/arXiv.2106.11959>, among others. Helper functions
are also included to create space-filling grids for tuning parameters that
are defined on a per-layer basis. These functions define the model
interfaces; the computations are carried out by separate engine packages.

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
