%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesMultiMode
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Testing and Detecting Multimodality using Bayesian Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggh4x 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-Rdpack 

%description
The testing approach works in two stages. First, a mixture distribution is
fitted on the data using a Sparse Finite Mixture (SFM) Markov chain Monte
Carlo (MCMC) algorithm following Malsiner-Walli, Frühwirth-Schnatter and
Grün (2016) <doi:10.1007/s11222-014-9500-2>). The number of mixture
components does not have to be specified; it is estimated simultaneously
with the mixture weights and components through the SFM approach. Second,
the resulting MCMC output is used to calculate the number of modes and
their locations following Basturk, Hoogerheide and van Dijk (2021)
<doi:10.2139/ssrn.3783351>. Posterior probabilities are retrieved for both
of these quantities providing a powerful tool for mode inference.
Currently the package supports a flexible mixture of shifted Poisson
distributions (see Basturk, Hoogerheide and van Dijk (2021)
<doi:10.2139/ssrn.3783351>).

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
