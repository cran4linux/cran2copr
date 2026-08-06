%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  trialSizing
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Experimental Design Sizing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 

%description
Sizes field experiments from uniformity-trial data, following the
relationship between the coefficient of variation and plot size. Checks a
trial for the spatial structure the sizing methods assume (semivariogram,
Moran's I, kriged field map), summarises the coefficient of variation over
every plot shape the grid admits, and estimates the optimal plot size by
the modified maximum curvature method of Meier and Lessman (1971), by the
linear response plateau (LRP) and quadratic response plateau (QRP) models,
and by the closed form of Paranaiba, Ferreira and Morais (2009), which can
be compared side by side. From the coefficient of variation at the optimum
it derives the number of replications needed to detect a given difference
between treatment means, as in Cargnelutti Filho and others (2014). Every
method returns standardised diagnostic statistics, optional bootstrap
uncertainty for the breakpoint, and publication-style plots.

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
