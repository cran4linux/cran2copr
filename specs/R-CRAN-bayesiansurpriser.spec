%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesiansurpriser
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Surprise for De-Biasing Thematic Maps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-scales >= 1.3.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-scales >= 1.3.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RColorBrewer 

%description
Implements Bayesian Surprise methodology for data visualization, based on
Correll and Heer (2017) <doi:10.1109/TVCG.2016.2598839> "Surprise!
Bayesian Weighting for De-Biasing Thematic Maps". Provides tools to weight
event data relative to spatio-temporal models, highlighting unexpected
patterns while de-biasing against known factors like population density or
sampling variation. Integrates seamlessly with 'sf' for spatial data and
'ggplot2' for visualization. Supports temporal/streaming data analysis.

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
