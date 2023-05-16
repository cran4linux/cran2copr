%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ActuarialM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Actuarial Measures Using Bell G Family

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
It computes two frequently applied actuarial measures, the expected
shortfall and the value at risk. Seven well-known classical distributions
in connection to the Bell generalized family are used as follows:
Bell-exponential distribution, Bell-extended exponential distribution,
Bell-Weibull distribution, Bell-extended Weibull distribution, Bell-Lomax
distribution, Bell-Burr-12 distribution, and Bell-Burr-X distribution.
Related works include: a) Fayomi, A., Tahir, M. H., Algarni, A., Imran,
M., & Jamal, F. (2022). "A new useful exponential model with applications
to quality control and actuarial data". Computational Intelligence and
Neuroscience, 2022. <doi:10.1155/2022/2489998>. b) Alsadat, N., Imran, M.,
Tahir, M. H., Jamal, F., Ahmad, H., & Elgarhy, M. (2023). "Compounded
Bell-G class of statistical models with applications to COVID-19 and
actuarial data". Open Physics, 21(1), 20220242.
<doi:10.1515/phys-2022-0242>.

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
