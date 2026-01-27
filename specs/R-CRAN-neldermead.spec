%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  neldermead
%global packver   1.0-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.13
Release:          1%{?dist}%{?buildtag}
Summary:          R Port of the 'Scilab' Neldermead Module

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-optimbase >= 1.0.9
BuildRequires:    R-CRAN-optimsimplex >= 1.0.7
BuildRequires:    R-methods 
Requires:         R-CRAN-optimbase >= 1.0.9
Requires:         R-CRAN-optimsimplex >= 1.0.7
Requires:         R-methods 

%description
Provides several direct search optimization algorithms based on the
simplex method. The provided algorithms are direct search algorithms, i.e.
algorithms which do not use the derivative of the cost function. They are
based on the update of a simplex. The following algorithms are available:
the fixed shape simplex method of Spendley, Hext and Himsworth
(unconstrained optimization with a fixed shape simplex, 1962)
<doi:10.1080/00401706.1962.10490033>, the variable shape simplex method of
Nelder and Mead (unconstrained optimization with a variable shape simplex
made, 1965) <doi:10.1093/comjnl/7.4.308>, and Box's complex method
(constrained optimization with a variable shape simplex, 1965) <doi:
10.1093/comjnl/8.1.42>.

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
