%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MTAFT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data-Driven Estimation for Multi-Threshold Accelerate Failure Time Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-grpreg 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-grpreg 

%description
Developed a data-driven estimation framework for the multi-threshold
accelerate failure time (MTAFT) model. The MTAFT model features different
linear forms in different subdomains, and one of the major challenges is
determining the number of threshold effects. The package introduces a
data-driven approach that utilizes a Schwarz' information criterion, which
demonstrates consistency under mild conditions. Additionally, a
cross-validation (CV) criterion with an order-preserved sample-splitting
scheme is proposed to achieve consistent estimation, without the need for
additional parameters. The package establishes the asymptotic properties
of the parameter estimates and includes an efficient score-type test to
examine the existence of threshold effects. The methodologies are
supported by numerical experiments and theoretical results, showcasing
their reliable performance in finite-sample cases.

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
