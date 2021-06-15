%global packname  epifitter
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis and Simulation of Plant Disease Progress Curves

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 

%description
Analysis and visualization of plant disease progress curve data. Functions
for fitting two-parameter population dynamics models (exponential,
monomolecular, logistic and Gompertz) to proportion data for single or
multiple epidemics using either linear or no-linear regression.
Statistical and visual outputs are provided to aid in model selection.
Synthetic curves can be simulated for any of the models given the
parameters. See Laurence V. Madden, Gareth Hughes, and Frank van den Bosch
(2007) <doi:10.1094/9780890545058> for further information on the methods.

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
