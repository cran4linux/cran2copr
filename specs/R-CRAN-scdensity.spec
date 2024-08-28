%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scdensity
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Shape-Constrained Kernel Density Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-lpSolve 

%description
Implements methods for obtaining kernel density estimates subject to a
variety of shape constraints (unimodality, bimodality, symmetry, tail
monotonicity, bounds, and constraints on the number of inflection points).
Enforcing constraints can eliminate unwanted waves or kinks in the
estimate, which improves its subjective appearance and can also improve
statistical performance. The main function scdensity() is very similar to
the density() function in 'stats', allowing shape-restricted estimates to
be obtained with little effort. The methods implemented in this package
are described in Wolters and Braun (2017)
<doi:10.1080/03610918.2017.1288247>, Wolters (2012)
<doi:10.18637/jss.v047.i06>, and Hall and Huang (2002)
<https://www3.stat.sinica.edu.tw/statistica/j12n4/j12n41/j12n41.htm>. See
the scdensity() help for for full citations.

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
