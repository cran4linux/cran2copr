%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gofgamma
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Tests for the Gamma Distribution

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
We implement various classical tests for the composite hypothesis of
testing the fit to the family of gamma distributions as the
Kolmogorov-Smirnov test, the Cramer-von Mises test, the Anderson Darling
test and the Watson test. For each test a parametric bootstrap procedure
is implemented, as considered in Henze, Meintanis & Ebner (2012)
<doi:10.1080/03610926.2010.542851>. The recent procedures presented in
Henze, Meintanis & Ebner (2012) <doi:10.1080/03610926.2010.542851> and
Betsch & Ebner (2019) <doi:10.1007/s00184-019-00708-7> are implemented.
Estimation of parameters of the gamma law are implemented using the method
of Bhattacharya (2001) <doi:10.1080/00949650108812100>.

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
