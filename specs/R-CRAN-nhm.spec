%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nhm
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Homogeneous Markov and Hidden Markov Multistate Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-mvtnorm 

%description
Fits non-homogeneous Markov multistate models and misclassification-type
hidden Markov models in continuous time to intermittently observed data.
Implements the methods in Titman (2011)
<doi:10.1111/j.1541-0420.2010.01550.x>. Uses direct numerical solution of
the Kolmogorov forward equations to calculate the transition
probabilities.

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
