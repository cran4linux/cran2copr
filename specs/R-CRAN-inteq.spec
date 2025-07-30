%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  inteq
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Numerical Solution of Integral Equations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
An R implementation of Matthew Thomas's 'Python' library 'inteq'. First,
this solves Fredholm integral equations of the first kind ($f(s) =
int_a^b K(s, y) g(y) dy$) using methods described by Twomey (1963)
<doi:10.1145/321150.321157>. Second, this solves Volterra integral
equations of the first kind ($f(s) = int_0^s K(s,y) g(t) dt$) using
methods from Betto and Thomas (2021) <doi:10.48550/arXiv.2106.08496>.
Third, this solves Voltera integral equations of the second kind ($g(s) =
f(s) + int_a^s K(s,y) g(y) dy$) using methods from Linz (1969)
<doi:10.1137/0706034>.

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
