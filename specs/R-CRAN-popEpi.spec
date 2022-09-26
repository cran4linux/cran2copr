%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  popEpi
%global packver   0.4.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.10
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Epidemiological Analysis using Population Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Epi >= 2.0
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-Epi >= 2.0
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-splines 
Requires:         R-CRAN-survival 

%description
Enables computation of epidemiological statistics, including those where
counts or mortality rates of the reference population are used.  Currently
supported: excess hazard models (Dickman, Sloggett, Hills, and Hakulinen
(2012) <doi:10.1002/sim.1597>), rates, mean survival times, relative/net
survival (in particular the Ederer II (Ederer and Heise (1959)) and Pohar
Perme (Pohar Perme, Stare, and Esteve (2012)
<doi:10.1111/j.1541-0420.2011.01640.x>) estimators), and standardized
incidence and mortality ratios, all of which can be easily adjusted for by
covariates such as age. Fast splitting and aggregation of 'Lexis' objects
(from package 'Epi') and other computations achieved using 'data.table'.

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
