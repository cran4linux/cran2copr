%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diffeqr
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Solving Differential Equations (ODEs, SDEs, DDEs, DAEs)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-JuliaCall 
Requires:         R-CRAN-JuliaCall 

%description
An interface to 'DifferentialEquations.jl' <https://diffeq.sciml.ai/dev/>
from the R programming language. It has unique high performance methods
for solving ordinary differential equations (ODE), stochastic differential
equations (SDE), delay differential equations (DDE),
differential-algebraic equations (DAE), and more. Much of the
functionality, including features like adaptive time stepping in SDEs, are
unique and allow for multiple orders of magnitude speedup over more common
methods. 'diffeqr' attaches an R interface onto the package, allowing
seamless use of this tooling by R users. For more information, see
Rackauckas and Nie (2017) <doi:10.5334/jors.151>.

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
