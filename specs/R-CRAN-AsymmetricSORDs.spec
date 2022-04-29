%global __brp_check_rpaths %{nil}
%global packname  AsymmetricSORDs
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Asymmetric Second Order Rotatable Designs (AsymmetricSORDs)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Response surface designs (RSDs) are widely used for Response Surface
Methodology (RSM) based optimization studies, which aid in exploring the
relationship between a group of explanatory variables and one or more
response variable(s) (G.E.P. Box and K.B. Wilson (1951), "On the
experimental attainment of optimum conditions" ; M. Hemavathi, Shashi
Shekhar, Eldho Varghese, Seema Jaggi, Bikas Sinha & Nripes Kumar Mandal
(2022) <DOI: 10.1080/03610926.2021.1944213>."Theoretical developments in
response surface designs: an informative review and further thoughts".).
Second order rotatable designs are the most prominent and popular class of
designs used for process and product optimization trials but it is
suitable for situations when all the number of levels for each factor is
the same. In many practical situations, RSDs with asymmetric levels (J.S.
Mehta and M.N. Das (1968). "Asymmetric rotatable designs and orthogonal
transformations" ; M. Hemavathi, Eldho Varghese, Shashi Shekhar & Seema
Jaggi (2020) <DOI: 10.1080/02664763.2020.1864817>. "Sequential asymmetric
third order rotatable designs (SATORDs)" .) are more suitable as these
designs explore more regions in the design space.This package contains
functions named Asords() ,CCD_coded(), CCD_original(), SORD_coded() and
SORD_original() for generating asymmetric/symmetric RSDs along with the
randomized layout. It also contains another function named Pred.var() for
generating the variance of predicted response as well as the moment matrix
based on a second order model.

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
