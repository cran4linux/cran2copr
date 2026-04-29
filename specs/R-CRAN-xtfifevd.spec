%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xtfifevd
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Panel Fixed Effects Filtered and Variance Decomposition Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-MASS 

%description
Implements fixed effects estimators for time-invariant variables in panel
data models. Provides three estimation methods: FEVD (Fixed Effects Vector
Decomposition) from Plumper and Troeger (2007) <doi:10.1093/pan/mpm002>,
and FEF (Fixed Effects Filtered) and FEF-IV (instrumental variables
variant) from Pesaran and Zhou (2018) <doi:10.1080/07474938.2016.1222225>.
All methods use the correct Pesaran-Zhou variance estimators that account
for generated regressor uncertainty, avoiding the size distortions
documented in the literature.

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
