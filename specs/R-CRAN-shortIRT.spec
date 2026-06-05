%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shortIRT
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Procedures Based on Item Response Theory Models for the Development of Short Test Forms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
Implement different Item Response Theory (IRT) based procedures for the
development of tests from item bank. The procedures are flexible enough to
be adopted for the development of short forms of full-length tests.
Different procedures are considered (Epifania, Anselmi & Robusto, 2022
<doi:10.1007/978-3-031-27781-8_7> and Epifania & Finos, 2025
<doi:10.1007/978-3-031-95995-0_32>). The main difference between the
presented procedures refers to the degree of control that they allow for
targeting specific latent trait levels. The simplest procedure, denoted as
benchmark procedure, does not allow for any control on the latent trait
levels of interest, while the other procedures allow for specifying either
discrete latent trait levels for which the information needs to be
maximized (theta-target procedure, <doi:10.1007/978-3-031-27781-8_7>) or a
target information function that needs to be recreated with the selected
items (item selection algorithm -ISA- denoted as Frank in
<doi:10.1007/978-3-031-95995-0_32>). Another difference concerns the
definition of the number of items to be selected. In the benchmark and
theta-target procedures, the number of items must be defined a priori,
while in ISA the number of items is determined automatically by the
algorithm.

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
