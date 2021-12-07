%global __brp_check_rpaths %{nil}
%global packname  PSPManalysis
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Physiologically Structured Population Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-pkgbuild >= 1.1
BuildRequires:    R-CRAN-rstudioapi >= 0.11
Requires:         R-CRAN-pkgbuild >= 1.1
Requires:         R-CRAN-rstudioapi >= 0.11

%description
Performs demographic, bifurcation and evolutionary analysis of
physiologically structured population models, which is a class of models
that consistently translates continuous-time models of individual life
history to the population level. A model of individual life history has to
be implemented specifying the individual-level functions that determine
the life history, such as development and mortality rates and fecundity.
M.A. Kirkilionis, O. Diekmann, B. Lisser, M. Nool, B. Sommeijer & A.M. de
Roos (2001) <doi:10.1142/S0218202501001264>. O.Diekmann, M.Gyllenberg &
J.A.J.Metz (2003) <doi:10.1016/S0040-5809(02)00058-8>. A.M. de Roos (2008)
<doi:10.1111/j.1461-0248.2007.01121.x>.

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
