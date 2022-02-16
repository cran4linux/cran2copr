%global __brp_check_rpaths %{nil}
%global packname  jaatha
%global packver   3.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Based Maximum Likelihood Parameter Estimation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.1.1
BuildRequires:    R-CRAN-assertthat >= 0.1
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.1.1
Requires:         R-CRAN-assertthat >= 0.1
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
An estimation method that can use computer simulations to approximate
maximum-likelihood estimates even when the likelihood function can not be
evaluated directly. It can be applied whenever it is feasible to conduct
many simulations, but works best when the data is approximately Poisson
distributed. It was originally designed for demographic inference in
evolutionary biology (Naduvilezhath et al., 2011
<doi:10.1111/j.1365-294X.2011.05131.x>, Mathew et al., 2013
<doi:10.1002/ece3.722>). It has optional support for conducting coalescent
simulation using the 'coala' package.

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
