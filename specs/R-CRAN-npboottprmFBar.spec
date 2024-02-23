%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npboottprmFBar
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Informative Nonparametric Bootstrap Test with Pooled Resampling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-lmPerm 
BuildRequires:    R-CRAN-npboottprm 
BuildRequires:    R-CRAN-restriktor 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-lmPerm 
Requires:         R-CRAN-npboottprm 
Requires:         R-CRAN-restriktor 

%description
Sample sizes are often small due to hard to reach target populations, rare
target events, time constraints, limited budgets, or ethical
considerations. Two statistical methods with promising performance in
small samples are the nonparametric bootstrap test with pooled resampling
method, which is the focus of Dwivedi, Mallawaarachchi, and Alvarado
(2017) <doi:10.1002/sim.7263>, and informative hypothesis testing, which
is implemented in the 'restriktor' package. The 'npboottprmFBar' package
uses the nonparametric bootstrap test with pooled resampling method to
implement informative hypothesis testing. The bootFbar() function can be
used to analyze data with this method and the persimon() function can be
used to conduct performance simulations on type-one error and statistical
power.

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
