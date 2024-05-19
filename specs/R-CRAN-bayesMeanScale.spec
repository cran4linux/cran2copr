%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesMeanScale
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Post-Estimation on the Mean Scale

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-posterior >= 1.5.0
BuildRequires:    R-CRAN-data.table >= 1.15.2
BuildRequires:    R-CRAN-bayestestR >= 0.13.2
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-posterior >= 1.5.0
Requires:         R-CRAN-data.table >= 1.15.2
Requires:         R-CRAN-bayestestR >= 0.13.2

%description
Computes Bayesian posterior distributions of predictions, marginal
effects, and differences of marginal effects for various generalized
linear models. Importantly, the posteriors are on the mean (response)
scale, allowing for more natural interpretation than summaries on the link
scale. Also, predictions and marginal effects of the count probabilities
for Poisson and negative binomial models can be computed.

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
