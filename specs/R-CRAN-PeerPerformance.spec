%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PeerPerformance
%global packver   2.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Luck-Corrected Peer Performance Analysis in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lmtest 
Requires:         R-parallel 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 

%description
Provides functions to perform the peer performance analysis of funds'
returns as described in Ardia and Boudt (2018)
<doi:10.1016/j.jbankfin.2017.10.014>. For each fund, the package estimates
the proportion of peers it outperforms, is equalled by, and is
outperformed by, correcting for luck with the false discovery approach of
Storey (2002) <doi:10.1111/1467-9868.00346>. Screenings can be based on
factor-model alphas, Sharpe ratios, or modified Sharpe ratios, the latter
using the equality test of Ardia and Boudt (2015)
<doi:10.1016/j.frl.2015.02.008>. Funds can be screened within a universe
or against a separate peer group, over rolling windows, and results come
with peer-bootstrap intervals, summary, plot, and tidy data frame methods.

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
