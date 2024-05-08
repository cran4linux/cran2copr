%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lotterybr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Lottery Datasets from Caixa Economica Federal

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A collection of functions designed to streamline the retrieval of data
from Brazilian lottery games operated by Caixa Econômica Federal,
accessible through the official website at
<https://loterias.caixa.gov.br/Paginas/default.aspx/>. Datasets for each
game are conveniently stored on the GitHub page at
<https://github.com/tomasbp2/LotteryBrasilDATA/>. Each game within this
repository consists of two primary datasets: the winners dataset and the
numbers dataset. The winners dataset includes crucial information such as
the draw date, game type, potential matches, winners for each match, and
corresponding prize amounts. Meanwhile, the numbers dataset provides
essential details including the draw date, game type, and the numbers
drawn during the respective lottery event. By offering easy access to
these datasets, the package facilitates efficient data retrieval and
analysis for researchers, analysts, and enthusiasts interested in
exploring the dynamics and outcomes of Brazilian lottery games.

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
