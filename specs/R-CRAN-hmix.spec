%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hmix
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Hidden Markov Model for Predicting Time Sequences with Mixture Sampling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gld >= 2.6.6
BuildRequires:    R-CRAN-cubature >= 2.1.0
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-glogis >= 1.0.2
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-HMM >= 1.0.1
BuildRequires:    R-CRAN-normalp >= 0.7.2
BuildRequires:    R-CRAN-edfun >= 0.2.0
BuildRequires:    R-CRAN-mc2d >= 0.2.0
Requires:         R-CRAN-gld >= 2.6.6
Requires:         R-CRAN-cubature >= 2.1.0
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-glogis >= 1.0.2
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-HMM >= 1.0.1
Requires:         R-CRAN-normalp >= 0.7.2
Requires:         R-CRAN-edfun >= 0.2.0
Requires:         R-CRAN-mc2d >= 0.2.0

%description
An algorithm for time series analysis that leverages hidden Markov models,
cluster analysis, and mixture distributions to segment data, detect
patterns and predict future sequences.

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
