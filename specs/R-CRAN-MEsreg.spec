%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MEsreg
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Maximum Entropy Estimation for Smooth Transition and Kink Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rsolnp 
Requires:         R-stats 

%description
Implements generalized maximum entropy estimation for linear regression,
kink regression, and smooth transition kink regression models. The
approach represents unknown parameters and disturbances as probability
distributions over discrete support spaces and estimates them by
maximizing entropy subject to model constraints. It is particularly suited
to ill-posed problems and does not require distributional assumptions on
the error term. The methods have been applied in empirical studies such as
Tarkhamtham and Yamaka (2019)
<https://thaijmath.com/index.php/thaijmath/article/view/867/870> and
Maneejuk, Yamaka, and Sriboonchitta (2022)
<doi:10.1080/03610918.2020.1836214>.

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
