%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RRgeo
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Species Distribution Modelling for Rare Species

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-biomod2 >= 4.2
BuildRequires:    R-CRAN-ecospat >= 3.2.1
BuildRequires:    R-CRAN-dismo >= 1.3
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Rphylopars 
BuildRequires:    R-CRAN-RRphylo 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-adehabitatMA 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-PresenceAbsence 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-leastcostpath 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-utils 
Requires:         R-CRAN-biomod2 >= 4.2
Requires:         R-CRAN-ecospat >= 3.2.1
Requires:         R-CRAN-dismo >= 1.3
Requires:         R-CRAN-ape 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Rphylopars 
Requires:         R-CRAN-RRphylo 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-adehabitatMA 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-PresenceAbsence 
Requires:         R-parallel 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-leastcostpath 
Requires:         R-CRAN-doSNOW 
Requires:         R-utils 

%description
Performs species distribution modeling for rare species with unprecedented
accuracy (Mondanaro et al., 2023 <doi:10.1111/2041-210X.14066>) and finds
the area of origin of species and past contact between them taking
climatic variability in full consideration (Mondanaro et al., 2025
<doi:10.1111/2041-210X.14478>).

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
