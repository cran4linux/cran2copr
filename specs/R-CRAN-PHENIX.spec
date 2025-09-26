%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PHENIX
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Phenotypic Integration Index

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-CRAN-SuppDists 
Requires:         R-CRAN-ppcor 
Requires:         R-CRAN-SuppDists 

%description
Provides functions to estimate the size-controlled phenotypic integration
index, a novel method by Torices & Méndez (2014) <doi:10.1086/676622> to
solve problems due to individual size when estimating integration (namely,
larger individuals have larger components, which will drive a correlation
between components only due to resource availability that might obscure
the observed measures of integration). In addition, the package also
provides the classical estimation by Wagner (1984)
<doi:10.1007/BF00275224>, bootstrapping and jackknife methods to calculate
confidence intervals and a significance test for both integration indices.
Further details can be found in Torices & Muñoz-Pajares
<doi:10.3732/apps.1400104>.

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
