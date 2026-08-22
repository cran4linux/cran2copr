%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phontrast
%global packver   2.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Contrast and Separation Metrics for Phonological Categories

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Computes and compares multiple measures of separation and overlap between
phonological categories (for example vowels or consonants) in arbitrary
multi-dimensional acoustic spaces such as formant values, mel-frequency
cepstral coefficients (MFCCs), duration, or learned embeddings. The main
entry point, phontrast(), reports several contrast metrics in one call --
Jensen-Shannon divergence and distance (Lin, 1991) <doi:10.1109/18.61115>,
the Pillai-Bartlett trace, Bhattacharyya distance and affinity,
Mahalanobis distance, and proportional overlap -- globally or by group on
a common separation-oriented scale, with bootstrap confidence intervals.
Also provides utilities for preparing estimates for downstream modelling
such as generalized additive models and mixed-effects models. Formerly
released as 'phonJSD'.

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
