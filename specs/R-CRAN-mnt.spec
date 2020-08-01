%global packname  mnt
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Affine Invariant Tests of Multivariate Normality

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-utils 
Requires:         R-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-utils 

%description
Various affine invariant multivariate normality tests are provided. It is
designed to accompany the survey article Ebner, B. and Henze, N. (2020)
<arXiv:2004.07332> titled "Tests for multivariate normality -- a critical
review with emphasis on weighted L^2-statistics". We implement new and
time honoured L^2-type tests of multivariate normality, such as the
Baringhaus-Henze-Epps-Pulley (BHEP) test, the Henze-Zirkler test, the test
of Henze-Jiménes-Gamero, the test of Henze-Jiménes-Gamero-Meintanis, the
test of Henze-Visage, the Dörr-Ebner-Henze test based on harmonic
oscillator and the Dörr-Ebner-Henze test based on a double estimation in a
PDE. Secondly, we include the measures of multivariate skewness and
kurtosis by Mardia, Koziol, Malkovich and Afifi and Móri, Rohatgi and
Székely, as well as the associated tests. Thirdly, we include the tests of
multivariate normality by Cox and Small, the 'energy' test of Székely and
Rizzo, the tests based on spherical harmonics by Manzotti and Quiroz and
the test of Pudelko. All the functions and tests need the data to be a n x
d matrix where n is the samplesize (number of rows) and d is the dimension
(number of columns).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
