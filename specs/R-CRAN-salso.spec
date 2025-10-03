%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  salso
%global packver   0.3.57
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.57
Release:          1%{?dist}%{?buildtag}
Summary:          Search Algorithms and Loss Functions for Bayesian Clustering

License:          MIT + file LICENSE | Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cargo
BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0

%description
The SALSO algorithm is an efficient randomized greedy search method to
find a point estimate for a random partition based on a loss function and
posterior Monte Carlo samples. The algorithm is implemented for many loss
functions, including the Binder loss and a generalization of the variation
of information loss, both of which allow for unequal weights on the two
types of clustering mistakes. Efficient implementations are also provided
for Monte Carlo estimation of the posterior expected loss of a given
clustering estimate. See Dahl, Johnson, Müller (2022)
<doi:10.1080/10618600.2022.2069779>.

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
