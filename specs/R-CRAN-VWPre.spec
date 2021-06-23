%global __brp_check_rpaths %{nil}
%global packname  VWPre
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Preprocessing Visual World Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.3.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-mgcv >= 1.8.16
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-tidyr >= 0.6.0
BuildRequires:    R-CRAN-shiny >= 0.14.2
BuildRequires:    R-CRAN-rlang >= 0.1.1
Requires:         R-stats >= 3.3.2
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-mgcv >= 1.8.16
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-tidyr >= 0.6.0
Requires:         R-CRAN-shiny >= 0.14.2
Requires:         R-CRAN-rlang >= 0.1.1

%description
Gaze data from the Visual World Paradigm requires significant
preprocessing prior to plotting and analyzing the data. This package
provides functions for preparing visual world eye-tracking data for
statistical analysis and plotting. It can prepare data for linear analyses
(e.g., ANOVA, Gaussian-family LMER, Gaussian-family GAMM) as well as
logistic analyses (e.g., binomial-family LMER and binomial-family GAMM).
Additionally, it contains various plotting functions for creating grand
average and conditional average plots. See the vignette for samples of the
functionality. Currently, the functions in this package are designed for
handling data collected with SR Research Eyelink eye trackers using Sample
Reports created in SR Research Data Viewer.  While we would like to add
functionality for data collected with other systems in the future, the
current package is considered to be feature-complete; further updates will
mainly entail maintenance and the addition of minor functionality.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
