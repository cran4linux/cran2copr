%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sequoia
%global packver   2.11.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.11.1
Release:          1%{?dist}%{?buildtag}
Summary:          Pedigree Inference from SNPs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-plyr >= 1.8.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-plyr >= 1.8.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-cli 

%description
Multi-generational pedigree inference from incomplete data on hundreds of
SNPs, including parentage assignment and sibship clustering. See Huisman
(2017) (<DOI:10.1111/1755-0998.12665>) for more information.

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
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
