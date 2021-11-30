%global __brp_check_rpaths %{nil}
%global packname  Copula.Markov
%global packver   2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Copula-Based Estimation and Statistical Process Control for Serially Correlated Time Series

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Estimation and statistical process control are performed under
copula-based time-series models. Available are statistical methods in Long
and Emura (2014 JCSA), Emura et al. (2017 Commun Stat-Simul)
<DOI:10.1080/03610918.2015.1073303>, Huang and Emura (2021 Commun
Stat-Simul) <DOI:10.1080/03610918.2019.1602647>, Lin et al. (2021 Comm
Stat-Simul) <DOI:10.1080/03610918.2019.1652318>, Sun et al. (2020 JSS
Series in Statistics)<DOI:10.1007/978-981-15-4998-4>, and Huang and Emura
(2021, in revision).

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
