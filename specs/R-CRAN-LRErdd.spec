%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LRErdd
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Discontinuity Designs as Local Randomized Experiments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-shiny 
Requires:         R-stats 

%description
A set of functions for the design and analysis of Regression Discontinuity
Designs as local randomized experiments within the potential outcome
approach as formalized in Li, Mattei and Mealli (2015)
<doi:10.1214/15-AOAS809>. A subset of functions implements the design
phase of the study, where the focus is on the selection of suitable
subpopulations for which valid causal inference can be drawn. These
functions provide summary statistics of pre- and post-treatment variables
by treatment status and select suitable subpopulations around the
threshold where pre-treatment variables are well balanced between
treatment groups, using randomization-based tests with adjustment for
multiplicities. Functions for a visual inspection of the results are also
provided. Finally, the package includes a set of functions for drawing
inference on causal effects for the selected subpopulations using
randomization-based modes of inference. Specifically, the Fisher Exact
p-value and Neyman approaches are implemented for the analysis of both
sharp and fuzzy Regression Discontinuity designs. The approach is
illustrated in a study concerning the effects of university grants on
student dropout.

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
