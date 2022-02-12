%global __brp_check_rpaths %{nil}
%global packname  monoreg
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Monotonic Regression Using a Marked Point Process Construction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0

%description
An extended version of the nonparametric Bayesian monotonic regression
procedure described in Saarela & Arjas (2011)
<DOI:10.1111/j.1467-9469.2010.00716.x>, allowing for multiple additive
monotonic components in the linear predictor, and time-to-event outcomes
through case-base sampling. The extension and its applications, including
estimation of absolute risks, are described in Saarela & Arjas (2015)
<DOI:10.1111/sjos.12125>. The package also implements the nonparametric
ordinal regression model described in Saarela, Rohrbeck & Arjas
<arXiv:2007.01390>.

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
