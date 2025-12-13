%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MixFrac
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fractional Factorial Designs with Alias and Trend-Free Analysis

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
Constructs mixed-level and regular fractional factorial designs using
coordinate-exchange optimization and automatic generator search. Design
quality is evaluated with J2 and balance (H-hat) criteria, alias
structures are computed via correlation-based chaining, and deterministic
trend-free run orders can be produced following Coster (1993)
<doi:10.1214/aos/1176349410>. Mixed-level design construction follows the
NONBPA approach of Pantoja-Pacheco et al. (2021)
<doi:10.3390/math9131455>. Regular fraction identification follows Guo,
Simpson and Pignatiello (2007) <doi:10.1080/00224065.2007.11917691>. Alias
structure computation follows Rios-Lira et al.(2021)
<doi:10.3390/math9233053>.

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
