%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cocotest
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Dependence Condition Test Using Ranked Correlation Coefficients

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-boot >= 1.1
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-boot >= 1.1

%description
A common misconception is that the Hochberg procedure comes up with
adequate overall type I error control when test statistics are positively
correlated. However, unless the test statistics follow some standard
distributions, the Hochberg procedure requires a more stringent positive
dependence assumption, beyond mere positive correlation, to ensure valid
overall type I error control. To fill this gap, we formulate statistical
tests grounded in rank correlation coefficients to validate fulfillment of
the positive dependence through stochastic ordering (PDS) condition. See
Gou, J., Wu, K. and Chen, O. Y. (2024). Rank correlation coefficient based
tests on positive dependence through stochastic ordering with application
in cancer studies, Technical Report.

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
