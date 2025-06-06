%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MSCsimtester
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tests of Multispecies Coalescent Gene Tree Simulator Output

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-kSamples 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-ape >= 5.0
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-kSamples 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
Statistical tests for validating multispecies coalescent gene tree
simulators, using pairwise distances and rooted triple counts. See Allman
ES, Baños HD, Rhodes JA 2023. Testing multispecies coalescent simulators
using summary statistics, IEEE/ACM Trans Comput Biol Bioinformat,
20(2):1613–1618. <doi:10.1109/TCBB.2022.3177956>.

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
