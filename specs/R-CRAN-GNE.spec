%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GNE
%global packver   0.99-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.6
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Generalized Nash Equilibria

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-SQUAREM 
BuildRequires:    R-methods 
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-SQUAREM 
Requires:         R-methods 

%description
Compute standard and generalized Nash Equilibria of non-cooperative games.
Optimization methods available are nonsmooth reformulation, fixed-point
formulation, minimization problem and constrained-equation reformulation.
See e.g. Kanzow and Facchinei (2010), <doi:10.1007/s10479-009-0653-x>.

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
