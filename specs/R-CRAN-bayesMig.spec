%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesMig
%global packver   0.4-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Projection of Migration

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bayesTFR 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-wpp2019 
Requires:         R-CRAN-bayesTFR 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-wpp2019 

%description
Producing probabilistic projections of net migration rate for all
countries of the world or for subnational units using a Bayesian
hierarchical model by Azose an Raftery (2015)
<doi:10.1007/s13524-015-0415-0>.

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
