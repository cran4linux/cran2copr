%global __brp_check_rpaths %{nil}
%global packname  TORDs
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Third Order Rotatable Designs (TORDs)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Third order response surface designs (M. Hemavathi, Shashi Shekhar, Eldho
Varghese, Seema Jaggi, Bikas Sinha & Nripes Kumar Mandal (2022)
<DOI:10.1080/03610926.2021.1944213>."Theoretical developments in response
surface designs: an informative review and further thoughts") are
classified into two types viz., designs which are suitable for sequential
experimentation and designs for non-sequential experimentation (M.
Hemavathi, Eldho Varghese, Shashi Shekhar & Seema Jaggi
(2022)<DOI:10.1080/02664763.2020.1864817>." Sequential asymmetric third
order rotatable designs (SATORDs)"). The sequential experimentation
approach involves conducting the trials step by step whereas, in the
non-sequential experimentation approach, the entire runs are executed in
one go.This package contains functions named STORDs() and NSTORDs() for
generating sequential/non-sequential TORDs given in Das, M. N., and V. L.
Narasimham (1962). <DOI:10.1214/aoms/1177704374>. "Construction of
rotatable designs through balanced incomplete block designs" along with
the randomized layout. It also contains another function named Pred3.var()
for generating the variance of predicted response as well as the moment
matrix based on a third order response surface model.

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
