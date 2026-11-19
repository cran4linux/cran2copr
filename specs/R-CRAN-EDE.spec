%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EDE
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extinction Date Estimation from Sighting Records

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Infers the extinction of a species from a time-ordered record of
sightings, collecting methods from the sighting-record and
stratigraphic-range literature under one interface. Includes endpoint
estimators (Robson & Whitlock, 1964; Strauss & Sadler, 1989; Roberts &
Solow, 2003), frequentist persistence tests (Solow, 1993a, 1993b; Burgman,
Grimson & Ferson, 1995; Solow & Roberts, 2003; Solow, 2005; McInerny,
Roberts, Davy & Cribb, 2006; Jarić & Ebenhard, 2010), Bayesian models
(Rout, Salomon & McCarthy, 2009; Caley & Barry, 2014; Alroy, 2014),
methods for sightings of uncertain reliability (Thompson et al., 2013;
Jarić & Roberts, 2014; Lee et al., 2014; Brook, Buettel & Jarić, 2019;
Kodikara et al., 2020, 2021), models combining records and surveys
(Thompson et al., 2017, 2019), and confidence intervals on the end-points
of fossil ranges (Marshall, 1994, 1997; Weiss & Marshall, 1999), a test of
a common end-point of several taxa (Solow, 1996), and an estimator of the
extinction time from radiometrically dated remains that allows for dating
error (Solow, 1997; Solow, Roberts & Robbirt, 2006; Bradshaw et al.,
2012). Also provides tools from extreme value theory, applied to the
latest sightings as upper order statistics: end-point estimators (Hall &
Wang, 1999; Dekkers, Einmahl & de Haan, 1989; Fraga Alves & Neves, 2014;
Smith, 1985), tests of whether a finite end-point is supported (Neves,
Picek & Fraga Alves, 2006; Hasofer & Wang, 1992), and an automatic choice
of the number of recent sightings. Where the source paper gives a worked
example the method is tested against it. All methods return a common
result class; persistence tests are inverted to give one-sided upper
confidence bounds.

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
