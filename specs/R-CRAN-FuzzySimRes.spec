%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FuzzySimRes
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation and Resampling Methods for Epistemic Fuzzy Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-FuzzyNumbers 
BuildRequires:    R-CRAN-palasso 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-FuzzyNumbers 
Requires:         R-CRAN-palasso 
Requires:         R-methods 

%description
Random simulations of fuzzy numbers are still a challenging problem. The
aim of this package is to provide the respective procedures to simulate
fuzzy random variables, especially in the case of the piecewise linear
fuzzy numbers (PLFNs, see Coroianua et al. (2013)
<doi:10.1016/j.fss.2013.02.005> for the further details). Additionally,
the special resampling algorithms known as the epistemic bootstrap are
provided (see Grzegorzewski and Romaniuk (2022)
<doi:10.34768/amcs-2022-0021>, Grzegorzewski and Romaniuk (2022)
<doi:10.1007/978-3-031-08974-9_39>) together with the functions to apply
statistical tests and estimate various characteristics based on the
epistemic bootstrap. The package also includes a real-life data set of
epistemic fuzzy triangular numbers. The fuzzy numbers used in this package
are consistent with the 'FuzzyNumbers' package.

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
