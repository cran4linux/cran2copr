%global __brp_check_rpaths %{nil}
%global packname  EcoTroph
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          An Implementation of the EcoTroph Ecosystem Modelling Approach

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-XML 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
An approach and software for modelling marine and freshwater ecosystems.
It is articulated entirely around trophic levels. EcoTroph's key displays
are bivariate plots, with trophic levels as the abscissa, and biomass
flows or related quantities as ordinates. Thus, trophic ecosystem
functioning can be modelled as a continuous flow of biomass surging up the
food web, from lower to higher trophic levels, due to predation and
ontogenic processes. Such an approach, wherein species as such disappear,
may be viewed as the ultimate stage in the use of the trophic level metric
for ecosystem modelling, providing a simplified but potentially useful
caricature of ecosystem functioning and impacts of fishing. This version
contains catch trophic spectrum analysis (CTSA) function and corrected
versions of the mf.diagnosis and create.ETmain functions.

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
