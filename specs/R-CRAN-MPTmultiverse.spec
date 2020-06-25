%global packname  MPTmultiverse
%global packver   0.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          Multiverse Analysis of Multinomial Processing Tree Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.1
Requires:         R-core >= 2.11.1
BuildArch:        noarch
BuildRequires:    R-CRAN-TreeBUGS >= 1.4.4
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MPTinR 
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-utils 
Requires:         R-CRAN-TreeBUGS >= 1.4.4
Requires:         R-parallel 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MPTinR 
Requires:         R-CRAN-runjags 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-limSolve 
Requires:         R-utils 

%description
Statistical or cognitive modeling usually requires a number of more or
less arbitrary choices creating one specific path through a 'garden of
forking paths'. The multiverse approach (Steegen, Tuerlinckx, Gelman, &
Vanpaemel, 2016, <doi:10.1177/1745691616658637>) offers a principled
alternative in which results for all possible combinations of reasonable
modeling choices are reported. MPTmultiverse performs a multiverse
analysis for multinomial processing tree (MPT, Riefer & Batchelder, 1988,
<doi:10.1037/0033-295X.95.3.318>) models combining
maximum-likelihood/frequentist and Bayesian estimation approaches with
different levels of pooling (i.e., data aggregation). For the frequentist
approaches, no pooling (with and without parametric or nonparametric
bootstrap) and complete pooling are implemented using MPTinR
<https://cran.r-project.org/package=MPTinR>. For the Bayesian approaches,
no pooling, complete pooling, and three different variants of partial
pooling are implemented using TreeBUGS
<https://cran.r-project.org/package=TreeBUGS>. The main function is
fit_mpt() who performs the multiverse analysis in one call.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
