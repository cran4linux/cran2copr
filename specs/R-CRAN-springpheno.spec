%global __brp_check_rpaths %{nil}
%global packname  springpheno
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spring Phenological Indices

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch

%description
Computes the extended spring indices (SI-x) and false spring exposure
indices (FSEI). The SI-x indices are standard indices used for analysis in
spring phenology studies. In addition, the FSEI is also from research on
the climatology of false springs and adjusted to include an early and late
false spring exposure index. The indices include the first leaf index,
first bloom index, and false spring exposure indices, along with all
calculations for all functions needed to calculate each index. The main
function returns all indices, but each function can also be run
separately. Allstadt et al. (2015) <doi: 10.1088/1748-9326/10/10/104008>
Ault et al. (2015) <doi: 10.1016/j.cageo.2015.06.015> Peterson and
Abatzoglou (2014) <doi: 10.1002/2014GL059266> Schwarz et al. (2006) <doi:
10.1111/j.1365-2486.2005.01097.x> Schwarz et al. (2013) <doi:
10.1002/joc.3625>.

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
