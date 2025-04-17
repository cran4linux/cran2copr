%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DoE.wrapper
%global packver   0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13
Release:          1%{?dist}%{?buildtag}
Summary:          Wrapper Package for Design of Experiments Functionality

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FrF2 >= 1.6.5
BuildRequires:    R-CRAN-AlgDesign >= 1.1
BuildRequires:    R-CRAN-DoE.base >= 0.23.4
BuildRequires:    R-CRAN-rsm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-DiceDesign 
Requires:         R-CRAN-FrF2 >= 1.6.5
Requires:         R-CRAN-AlgDesign >= 1.1
Requires:         R-CRAN-DoE.base >= 0.23.4
Requires:         R-CRAN-rsm 
Requires:         R-stats 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-DiceDesign 

%description
Various kinds of designs for (industrial) experiments can be created. The
package uses, and sometimes enhances, design generation routines from
other packages. So far, response surface designs from package 'rsm', Latin
hypercube samples from packages 'lhs' and 'DiceDesign', and D-optimal
designs from package 'AlgDesign' have been implemented.

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
