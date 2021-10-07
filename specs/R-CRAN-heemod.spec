%global __brp_check_rpaths %{nil}
%global packname  heemod
%global packver   0.14.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14.4
Release:          1%{?dist}%{?buildtag}
Summary:          Markov Models for Health Economic Evaluations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-tibble >= 3.0.6
BuildRequires:    R-CRAN-memoise >= 2.0.0
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-dplyr >= 1.0.4
BuildRequires:    R-CRAN-rlang >= 0.4.1
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-mvnfast >= 0.2.5
BuildRequires:    R-CRAN-lazyeval >= 0.2.2
BuildRequires:    R-CRAN-pryr >= 0.1.4
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-tibble >= 3.0.6
Requires:         R-CRAN-memoise >= 2.0.0
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-dplyr >= 1.0.4
Requires:         R-CRAN-rlang >= 0.4.1
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-mvnfast >= 0.2.5
Requires:         R-CRAN-lazyeval >= 0.2.2
Requires:         R-CRAN-pryr >= 0.1.4

%description
An implementation of the modelling and reporting features described in
reference textbook and guidelines (Briggs, Andrew, et al. Decision
Modelling for Health Economic Evaluation. Oxford Univ. Press, 2011;
Siebert, U. et al. State-Transition Modeling. Medical Decision Making 32,
690-700 (2012).): deterministic and probabilistic sensitivity analysis,
heterogeneity analysis, time dependency on state-time and model-time
(semi-Markov and non-homogeneous Markov models), etc.

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
