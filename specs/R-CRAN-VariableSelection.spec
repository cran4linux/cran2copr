%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VariableSelection
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Select Variables for Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.2.2
BuildRequires:    R-CRAN-GA >= 3.2.3
BuildRequires:    R-CRAN-memoise >= 2.0.1
Requires:         R-stats >= 4.2.2
Requires:         R-CRAN-GA >= 3.2.3
Requires:         R-CRAN-memoise >= 2.0.1

%description
Provides variable selection for linear models and generalized linear
models using Bayesian information criterion (BIC) and model posterior
probability (MPP). Given a set of candidate predictors, it evaluates
candidate models and returns model-level summaries (BIC and MPP) and
predictor-level posterior inclusion probabilities (PIP). For more details
see Xu, S., Ferreira, M. A., & Tegge, A. N. (2025)
<doi:10.48550/arXiv.2510.02628>.

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
