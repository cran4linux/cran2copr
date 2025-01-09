%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bivpois
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bivariate Poisson Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 

%description
Maximum likelihood estimation, random values generation, density
computation and other functions for the bivariate Poisson distribution.
References include: Kawamura K. (1984). "Direct calculation of maximum
likelihood estimator for the bivariate Poisson distribution". Kodai
Mathematical Journal, 7(2): 211--221. <doi:10.2996/kmj/1138036908>.
Kocherlakota S. and Kocherlakota K. (1992). "Bivariate discrete
distributions". CRC Press. <doi:10.1201/9781315138480>. Karlis D. and
Ntzoufras I. (2003). "Analysis of sports data by using bivariate Poisson
models". Journal of the Royal Statistical Society: Series D (The
Statistician), 52(3): 381--393. <doi:10.1111/1467-9884.00366>.

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
