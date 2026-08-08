%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EDE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extinction Date Estimation from Sighting Records

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch

%description
Estimates the historic date of extinction of a species from a time-ordered
record of sighting events. Given a table of sighting counts per year,
computes extinction date estimators from the sighting-record literature:
optimal linear estimation under a record-value model (Roberts & Solow,
2003), nonparametric and sighting-effort-weighted persistence tests
(Solow, 1993; Solow, 2005), a sighting-rate persistence test comparable
across records with different observation periods (McInerny, Roberts, Davy
& Cribb, 2006), a classical confidence interval on the end of a temporal
range (Strauss & Sadler, 1989), a truncation-point extrapolation (Robson &
Whitlock, 1964), and a combinatorial persistence test based on
inclusion-exclusion over sighting-gap occupancy (Burgman, Grimson &
Ferson, 1995). Every estimator is built on a single validated input object
and returns a common result class with, where defined, a point estimate, a
confidence interval, or a full persistence-probability curve.

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
