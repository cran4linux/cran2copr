%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  contdid
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Difference-in-Differences with a Continuous Treatment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BMisc >= 1.4.8
BuildRequires:    R-CRAN-ptetools 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-npiv 
Requires:         R-CRAN-BMisc >= 1.4.8
Requires:         R-CRAN-ptetools 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-splines2 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-npiv 

%description
Provides methods for difference-in-differences with a continuous treatment
and staggered treatment adoption. Includes estimation of treatment effects
and causal responses as a function of the dose, event studies indexed by
length of exposure to the treatment, and aggregation into overall average
effects. Uniform inference procedures are included, along with both
parametric and nonparametric models for treatment effects. The methods are
based on Callaway, Goodman-Bacon, and Sant'Anna (2025)
<doi:10.48550/arXiv.2107.02637>.

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
