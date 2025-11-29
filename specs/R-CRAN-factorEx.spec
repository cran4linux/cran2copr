%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  factorEx
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Design and Analysis for Factorial Experiments

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-genlasso 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-estimatr 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-genlasso 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-estimatr 

%description
Provides design-based and model-based estimators for the population
average marginal component effects in general factorial experiments,
including conjoint analysis. The package also implements a series of
recommendations offered in de la Cuesta, Egami, and Imai (2022)
<doi:10.1017/pan.2020.40>, and Egami and Imai (2019)
<doi:10.1080/01621459.2018.1476246>.

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
