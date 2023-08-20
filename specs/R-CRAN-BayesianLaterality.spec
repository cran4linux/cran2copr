%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesianLaterality
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Predict Brain Asymmetry Based on Handedness and Dichotic Listening

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tmvtnorm >= 1.4
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-tmvtnorm >= 1.4
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-Rdpack 

%description
Functional differences between the cerebral hemispheres are a fundamental
characteristic of the human brain. Researchers interested in studying
these differences often infer underlying hemispheric dominance for a
certain function (e.g., language) from laterality indices calculated from
observed performance or brain activation measures . However, any inference
from observed measures to latent (unobserved) classes has to consider the
prior probability of class membership in the population. The provided
functions implement a Bayesian model for predicting hemispheric dominance
from observed laterality indices (Sorensen and Westerhausen, Laterality:
Asymmetries of Body, Brain and Cognition, 2020,
<doi:10.1080/1357650X.2020.1769124>).

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
