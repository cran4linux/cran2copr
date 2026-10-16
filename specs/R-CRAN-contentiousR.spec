%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  contentiousR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Contentious Politics and Civil Conflict Research

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-states 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-states 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Constructs reproducible country-year panels for research on contentious
politics and civil conflict, as described in Guseinov (2026)
<doi:10.2139/ssrn.7506799>. Functions build state panels keyed by
Correlates of War or Gleditsch-Ward country codes and join curated
socioeconomic, leadership, democracy, conflict, protest, and
revolutionary-episode data on that common key, with diagnostics and plots
for comparing source coverage. Bundled sources include Gapminder; the
Nonviolent and Violent Campaigns and Outcomes (NAVCO) 2.1 data, Chenoweth
and Shay (2019) <doi:10.7910/DVN/MHOXDV>; the Social Conflict Analysis
Database, Salehyan et al. (2012) <doi:10.1080/03050629.2012.697426>; the
Uppsala Conflict Data Program and Peace Research Institute Oslo
(UCDP/PRIO) Armed Conflict Dataset, Gleditsch et al. (2002)
<doi:10.1177/0022343302039005007>; and the Major Episodes of Contention
data, Chenoweth and Kang (2026) <doi:10.1093/jopres/xjaf008>. Varieties of
Democracy (V-Dem) indicators require the optional 'vdemdata' package,
which is not on CRAN and can be installed from
<https://github.com/vdeminstitute/vdemdata>.

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
