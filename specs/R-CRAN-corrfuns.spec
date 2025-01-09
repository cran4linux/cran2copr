%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  corrfuns
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Correlation Coefficient Related Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 
Requires:         R-stats 

%description
Many correlation coefficient related functions are offered, such as
correlations, partial correlations and hypothesis testing using asymptotic
tests and computer intensive methods (bootstrap and permutation).
References include Mardia K.V., Kent J.T. and Bibby J.M. (1979).
"Multivariate Analysis". ISBN: 978-0124712522. London: Academic Press and
Owen A. B. (2001). "Empirical likelihood". Chapman and Hall/CRC Press.
ISBN: 9781584880714.

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
