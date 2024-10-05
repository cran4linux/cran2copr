%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FuzzyResampling
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Resampling Methods for Triangular and Trapezoidal Fuzzy Numbers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
The classical (i.e. Efron's, see Efron and Tibshirani (1994,
ISBN:978-0412042317) "An Introduction to the Bootstrap") bootstrap is
widely used for both the real (i.e. "crisp") and fuzzy data. The main aim
of the algorithms implemented in this package is to overcome a problem
with repetition of a few distinct values and to create fuzzy numbers,
which are "similar" (but not the same) to values from the initial sample.
To do this, different characteristics of triangular/trapezoidal numbers
are kept (like the value, the ambiguity, etc., see Grzegorzewski et al.
<doi:10.2991/eusflat-19.2019.68>, Grzegorzewski et al. (2020)
<doi:10.2991/ijcis.d.201012.003>, Grzegorzewski et al. (2020)
<doi:10.34768/amcs-2020-0022>, Grzegorzewski and Romaniuk (2022)
<doi:10.1007/978-3-030-95929-6_3>, Romaniuk and Hryniewicz (2019)
<doi:10.1007/s00500-018-3251-5>). Some additional procedures related to
these resampling methods are also provided, like calculation of the
Bertoluzza et al.'s distance (aka the mid/spread distance, see Bertoluzza
et al. (1995) "On a new class of distances between fuzzy numbers") and
estimation of the p-value of the one- and two- sample bootstrapped test
for the mean (see Lubiano et al. (2016,
<doi:10.1016/j.ejor.2015.11.016>)). Additionally, there are procedures
which randomly generate trapezoidal fuzzy numbers using some well-known
statistical distributions.

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
