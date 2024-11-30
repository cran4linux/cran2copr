%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  banditsCI
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bandit-Based Experiments and Policy Evaluation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.56
BuildRequires:    R-CRAN-glmnet >= 4.1.6
BuildRequires:    R-CRAN-Rdpack >= 2.6
BuildRequires:    R-CRAN-mvtnorm >= 1.2.2
Requires:         R-CRAN-MASS >= 7.3.56
Requires:         R-CRAN-glmnet >= 4.1.6
Requires:         R-CRAN-Rdpack >= 2.6
Requires:         R-CRAN-mvtnorm >= 1.2.2

%description
Frequentist inference on adaptively generated data. The methods
implemented are based on Zhan et al. (2021)
<doi:10.48550/arXiv.2106.02029> and Hadad et al. (2021)
<doi:10.48550/arXiv.1911.02768>. For illustration, several functions for
simulating non-contextual and contextual adaptive experiments using
Thompson sampling are also supplied.

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
