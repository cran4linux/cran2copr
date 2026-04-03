%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  radEmu
%global packver   2.3.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Using Relative Abundance Data to Estimate of Multiplicative Differences in Mean Absolute Abundance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 

%description
A differential abundance method for the analysis of microbiome data.
'radEmu' estimates fold-differences in the abundance of taxa across
samples relative to "typical" fold-differences. Notably, it does not
require pseudocounts, nor choosing a denominator taxon. For more details,
see Clausen et al. (2026) <doi:10.1093/biomet/asag009>.

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
