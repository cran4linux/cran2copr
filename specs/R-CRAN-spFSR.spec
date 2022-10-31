%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spFSR
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Selection and Ranking via Simultaneous Perturbation Stochastic Approximation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.4.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-future >= 1.28.0
BuildRequires:    R-CRAN-tictoc >= 1.0
BuildRequires:    R-CRAN-mlr3learners >= 0.5.4
BuildRequires:    R-CRAN-lgr >= 0.4.4
BuildRequires:    R-CRAN-mlr3pipelines >= 0.4.2
BuildRequires:    R-CRAN-mlr3 >= 0.14.0
Requires:         R-parallel >= 3.4.2
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-future >= 1.28.0
Requires:         R-CRAN-tictoc >= 1.0
Requires:         R-CRAN-mlr3learners >= 0.5.4
Requires:         R-CRAN-lgr >= 0.4.4
Requires:         R-CRAN-mlr3pipelines >= 0.4.2
Requires:         R-CRAN-mlr3 >= 0.14.0

%description
An implementation of feature selection, weighting and ranking via
simultaneous perturbation stochastic approximation (SPSA). The SPSA-FSR
algorithm searches for a locally optimal set of features that yield the
best predictive performance using some error measures such as mean squared
error (for regression problems) and accuracy rate (for classification
problems).

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
