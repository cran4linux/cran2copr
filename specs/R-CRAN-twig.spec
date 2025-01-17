%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  twig
%global packver   1.0.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          For Streamlining Decision and Economic Evaluation Models using Grammar of Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-doParallel 

%description
Provides tools for building decision and cost-effectiveness analysis
models. It enables users to write these models concisely, simulate
outcomes—including probabilistic analyses—efficiently using optimized
vectorized processes and parallel computing, and produce results. The
package employs a Grammar of Modeling approach, inspired by the Grammar of
Graphics, to streamline model construction. For an interactive graphical
user interface, see 'DecisionTwig' at
<https://www.dashlab.ca/projects/decision_twig/>. Comprehensive tutorials
and vignettes are available at <https://hjalal.github.io/twig/>.

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
