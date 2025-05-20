%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  inecolr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling and Plotting for Ecologist

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-betapart 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-gmodels 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tree 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-betapart 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-gmodels 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tree 
Requires:         R-CRAN-vegan 

%description
It provides multiple functions that are useful for ecological research and
teaching statistics to ecologists. It is based on data analysis courses
offered at the Instituto de Ecología AC (INECOL). For references and
published evidence see, Manrique-Ascencio, et al (2024)
<doi:10.1111/gcb.17282>, Manrique-Ascencio et al (2024)
<doi:10.1111/plb.13683>, Ruiz-Guerra et al(2017)
<doi:10.17129/botsci.812>, Juarez-Fragoso et al (2024)
<doi:10.1007/s10980-024-01809-z>, Papaqui-Bello et al (2024)
<doi:10.13102/sociobiology.v71i2.10503>.

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
