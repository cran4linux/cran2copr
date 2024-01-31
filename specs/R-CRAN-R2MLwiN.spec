%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  R2MLwiN
%global packver   0.8-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.9
Release:          1%{?dist}%{?buildtag}
Summary:          Running 'MLwiN' from Within R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreign >= 0.8.46
BuildRequires:    R-CRAN-digest >= 0.6.5
BuildRequires:    R-CRAN-coda >= 0.16.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-R2WinBUGS 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-memisc 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-foreign >= 0.8.46
Requires:         R-CRAN-digest >= 0.6.5
Requires:         R-CRAN-coda >= 0.16.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-R2WinBUGS 
Requires:         R-CRAN-texreg 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-memisc 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tibble 

%description
An R command interface to the 'MLwiN' multilevel modelling software
package.

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
