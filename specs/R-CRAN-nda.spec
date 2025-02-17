%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nda
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Network-Based Dimensionality Reduction and Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.00
Requires:         R-core >= 4.00
BuildArch:        noarch
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mco 
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-CRAN-lm.beta 
BuildRequires:    R-CRAN-leidenAlg 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-psych 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mco 
Requires:         R-CRAN-ppcor 
Requires:         R-CRAN-lm.beta 
Requires:         R-CRAN-leidenAlg 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-visNetwork 

%description
Non-parametric dimensionality reduction function. Reduction with and
without feature selection. Plot functions. Automated feature selections.
Kosztyan et. al. (2024) <doi:10.1016/j.eswa.2023.121779>.

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
