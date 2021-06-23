%global __brp_check_rpaths %{nil}
%global packname  RVCompare
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Compare Real Valued Random Variables

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 3.4.4
BuildRequires:    R-utils >= 3.4.4
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-pracma >= 2.2.2
Requires:         R-stats >= 3.4.4
Requires:         R-utils >= 3.4.4
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-pracma >= 2.2.2

%description
A framework with tools to compare two random variables, and determine
which of them produces lower values. It can compute the Cp and Cd of
theoretical of probability distributions, as explained in E. Arza (2021)
<https://github.com/EtorArza/RVCompare-paper/releases>. Given the observed
samples of two random variables X_A and X_B, it can compute the confidence
bands of the cumulative distributions of X'_A and X'_B (see E. Arza (2021)
<https://github.com/EtorArza/RVCompare-paper> for details) based on the
observed samples of X_A and X_B. Uses bootstrap and DKW-bounds to compute
the confidence bands of the cumulative distributions. These two methods
are described in B. Efron. (1979) <doi:10.1214/aos/1176344552> and P.
Massart (1990) <doi:10.1214/aop/1176990746>.

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
