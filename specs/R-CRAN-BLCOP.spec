%global __brp_check_rpaths %{nil}
%global packname  BLCOP
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Black-Litterman and Copula Opinion Pooling Frameworks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fPortfolio >= 3011.81
BuildRequires:    R-CRAN-RUnit >= 0.4.22
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-fMultivar 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-fPortfolio >= 3011.81
Requires:         R-CRAN-RUnit >= 0.4.22
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-fMultivar 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 

%description
An implementation of the Black-Litterman Model and Attilio Meucci's copula
opinion pooling framework as described in Meucci, Attilio (2005)
<doi:10.2139/ssrn.848407>, Meucci, Attilio (2006)
<doi:10.2139/ssrn.872577> and Meucci, Attilio (2008)
<doi:10.2139/ssrn.1117574>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
