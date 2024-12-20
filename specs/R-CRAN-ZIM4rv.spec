%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ZIM4rv
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Gene‐based Association Tests of Zero‐inflated Count Phenotype for Rare Variants

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SKAT 
BuildRequires:    R-CRAN-RNOmni 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-stats 
Requires:         R-CRAN-SKAT 
Requires:         R-CRAN-RNOmni 

%description
Gene‐based association tests to model count data with excessive zeros and
rare variants using zero-inflated Poisson/zero-inflated negative Binomial
regression framework. This method was originally described by Fan, Sun,
and Li in Genetic Epidemiology 46(1):73-86 <doi:10.1002/gepi.22438>.

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
