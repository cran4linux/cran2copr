%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rQCC
%global packver   2.22.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.22.12
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Quality Control Chart

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch

%description
Constructs various robust quality control charts based on the median or
Hodges-Lehmann estimator (location) and the median absolute deviation
(MAD) or Shamos estimator (scale). The estimators used for the robust
control charts are all unbiased with a sample of finite size. For more
details, see Park, Kim and Wang (2022)
<doi:10.1080/03610918.2019.1699114>. In addition, using this R package,
the conventional quality control charts such as X-bar, S, R, p, np, u, c,
g, h, and t charts are also easily constructed. This work was supported by
the National Research Foundation of Korea (NRF) grant funded by the Korea
government (MSIT) (No. 2022R1A2C1091319).

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
