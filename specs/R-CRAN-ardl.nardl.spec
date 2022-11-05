%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ardl.nardl
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Linear and Nonlinear Autoregressive Distributed Lag Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics >= 4.2.1
BuildRequires:    R-stats >= 4.2.1
BuildRequires:    R-CRAN-car >= 3.1.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-texreg >= 1.38.6
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-lmtest >= 0.9.38
BuildRequires:    R-CRAN-rlist >= 0.4.6.2
BuildRequires:    R-CRAN-tseries >= 0.10.51
BuildRequires:    R-CRAN-nardl >= 0.1.6
Requires:         R-graphics >= 4.2.1
Requires:         R-stats >= 4.2.1
Requires:         R-CRAN-car >= 3.1.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-texreg >= 1.38.6
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-lmtest >= 0.9.38
Requires:         R-CRAN-rlist >= 0.4.6.2
Requires:         R-CRAN-tseries >= 0.10.51
Requires:         R-CRAN-nardl >= 0.1.6

%description
Estimate the linear and nonlinear autoregressive distributed lag (ARDL &
NARDL) models and the corresponding error correction models, and test for
longrun and short-run asymmetric. The Pesaran, Shin & Smith (2001)
(<doi:10.1002/jae.616>) bounds test for level relationships is also
provided. The 'ardl.nardl' package also performs short-run and longrun
symmetric restrictions available at Shin et al. (2014)
<doi:10.1007/978-1-4899-8008-3_9> and their corresponding tests.

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
