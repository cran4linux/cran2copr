%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesMultiMode
%global packver   0.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Mode Inference

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.4
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MCMCglmm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 >= 3.3.4
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MCMCglmm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-Rdpack 

%description
A two-step Bayesian approach for mode inference following Cross,
Hoogerheide, Labonne and van Dijk (2024)
<doi:10.1016/j.econlet.2024.111579>). First, a mixture distribution is
fitted on the data using a sparse finite mixture (SFM) Markov chain Monte
Carlo (MCMC) algorithm. The number of mixture components does not have to
be known; the size of the mixture is estimated endogenously through the
SFM approach. Second, the modes of the estimated mixture at each MCMC draw
are retrieved using algorithms specifically tailored for mode detection.
These estimates are then used to construct posterior probabilities for the
number of modes, their locations and uncertainties, providing a powerful
tool for mode inference.

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
