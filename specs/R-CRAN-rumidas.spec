%global packname  rumidas
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Univariate GARCH-MIDAS, Double-Asymmetric GARCH-MIDAS and MEM-MIDAS

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.2
BuildRequires:    R-utils >= 4.0.2
BuildRequires:    R-CRAN-zoo >= 1.8.8
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-maxLik >= 1.3.8
BuildRequires:    R-CRAN-roll >= 1.1.4
BuildRequires:    R-CRAN-Rdpack >= 1.0
BuildRequires:    R-CRAN-highfrequency >= 0.6.5
BuildRequires:    R-CRAN-xts >= 0.12.0
BuildRequires:    R-CRAN-tseries >= 0.10.47
Requires:         R-stats >= 4.0.2
Requires:         R-utils >= 4.0.2
Requires:         R-CRAN-zoo >= 1.8.8
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-maxLik >= 1.3.8
Requires:         R-CRAN-roll >= 1.1.4
Requires:         R-CRAN-Rdpack >= 1.0
Requires:         R-CRAN-highfrequency >= 0.6.5
Requires:         R-CRAN-xts >= 0.12.0
Requires:         R-CRAN-tseries >= 0.10.47

%description
Adds the MIxing-Data Sampling (MIDAS, Ghysels et al. (2007)
<doi:10.1080/07474930600972467>) components to a variety of GARCH and MEM
(Engle (2002) <doi:10.1002/jae.683>) models, with the aim of predicting
the volatility with additional low-frequency (that is, MIDAS) terms. The
estimation takes place through simple functions, which provide in-sample
and (if present) and out-of-sample evaluations. 'rumidas' also offers a
summary tool, which synthesizes the main information of the estimated
model. There is also the possibility of generating one-step-ahead and
multi-step-ahead forecasts.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
