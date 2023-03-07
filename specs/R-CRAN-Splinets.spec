%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Splinets
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Data Analysis using Splines and Orthogonal Spline Bases

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-methods 
Requires:         R-graphics 

%description
Splines are efficiently represented through their Taylor expansion at the
knots. The representation accounts for the support sets and is thus
suitable for sparse functional data. Two cases of boundary conditions are
considered: zero-boundary or periodic-boundary for all derivatives except
the last. The periodical splines are represented graphically using polar
coordinates. The B-splines and orthogonal bases of splines that reside on
small total support are implemented. The orthogonal bases are referred to
as 'splinets' and are utilized for functional data analysis. Random spline
generator is implemented as well as all fundamental algebraic and calculus
operations on splines.  The optimal, in the least square sense, functional
fit by 'splinets' to data consisting of sampled values of functions as
well as splines build over another set of knots is obtained and used for
functional data analysis.  <arXiv:2102.00733>,
<doi:10.1016/j.cam.2022.114444>, <arXiv:2302.07552>.

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
