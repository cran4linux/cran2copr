%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kindling
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Higher-Level Interface of 'torch' Package to Auto-Train Neural Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-parsnip >= 1.0.0
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-NeuralNetTools 
BuildRequires:    R-CRAN-vip 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-dials 
Requires:         R-CRAN-parsnip >= 1.0.0
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-NeuralNetTools 
Requires:         R-CRAN-vip 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-dials 

%description
Provides a higher-level interface to the 'torch' package for defining,
training, and tuning neural networks. This package supports feedforward
(multi-layer perceptron) and recurrent neural networks (RNN (Recurrent
Neural Networks), LSTM (Long Short-Term Memory), GRU (Gated Recurrent
Unit)), and also reduces boilerplate code while enabling seamless
integration with 'torch'. The methods to train neural networks from this
package also bridges to titanic ML frameworks in R namely 'tidymodels'
ecosystem, enabling the 'parsnip' model specifications, workflows,
recipes, and tuning tools.

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
