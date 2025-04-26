%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cbsREPS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hedonic and Multilateral Index Methods for Real Estate Price Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-KFAS 
Requires:         R-CRAN-stringr 

%description
Compute price indices using various Hedonic and multilateral methods,
including Laspeyres, Paasche, Fisher, and HMTS (Hedonic Multilateral Time
series re-estimation with splicing). The central function
calculate_price_index() offers a unified interface for running these
methods on structured datasets. This package is designed to support index
construction workflows for real estate and other domains where
quality-adjusted price comparisons over time are essential. The
development of this package was funded by Eurostat and Statistics
Netherlands (CBS), and carried out by Statistics Netherlands. The HMTS
method implemented here is described in Ishaak, Ouwehand and Remøy (2024)
<doi:10.1177/0282423X241246617>. For broader methodological context, see
Eurostat (2013, ISBN:978-92-79-25984-5, <doi:10.2785/34007>).

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
