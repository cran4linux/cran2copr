%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AgriFusionR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Integration Framework for Agricultural Analytics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Assembles agricultural analyses around a single unit of observation, the
management unit within a season, and keeps climate, soil and
remote-sensing covariates aligned to it. Covariates are aggregated over
phenological windows derived from accumulated growing degree days rather
than calendar months, following McMaster and Wilhelm (1997)
<doi:10.1016/S0168-1923(97)00027-0>. Models are validated with spatial
resampling by default, since random cross-validation inflates apparent
skill when observations are spatially autocorrelated, as shown by Roberts
and others (2017) <doi:10.1111/ecog.02881>. Prediction intervals use split
conformal inference after Lei and others (2018)
<doi:10.1080/01621459.2017.1307116>. Data sources and learning algorithms
are supplied through registries so that new providers and methods can be
added without modifying the package.

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
