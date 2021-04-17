%global packname  gambin
%global packver   2.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit the Gambin Model to Species Abundance Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 

%description
Fits unimodal and multimodal gambin distributions to species-abundance
distributions from ecological data, as in in Matthews et al. (2014)
<DOI:10.1111/ecog.00861>. 'gambin' is short for 'gamma-binomial'. The main
function is fit_abundances(), which estimates the 'alpha' parameter(s) of
the gambin distribution using maximum likelihood. Functions are also
provided to generate the gambin distribution and for calculating
likelihood statistics.

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
