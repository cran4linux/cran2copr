%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dexisensitivity
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'DEXi' Decision Tree Analysis and Visualization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 3.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-AlgDesign 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-genalg 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-testthat >= 3.0.0
Requires:         R-methods 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-AlgDesign 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-genalg 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-xml2 

%description
Provides a versatile toolkit for analyzing and visualizing 'DEXi'
(Decision EXpert for education) decision trees, facilitating
multi-criteria decision analysis directly within R. Users can read .dxi
files, manipulate decision trees, and evaluate various scenarios. It
supports sensitivity analysis through Monte Carlo simulations,
one-at-a-time approaches, and variance-based methods, helping to discern
the impact of input variations. Additionally, it includes functionalities
for generating sampling plans and an array of visualization options for
decision trees and analysis results. A distinctive feature is the synoptic
table plot, aiding in the efficient comparison of scenarios. Whether for
in-depth decision modeling or sensitivity analysis, this package stands as
a comprehensive solution. Definition of sensitivity analyses available in
Carpani, Bergez and Monod (2012) <doi:10.1016/j.envsoft.2011.10.002> and
detailed description of the package soon available in Alaphilippe, Allart,
Carpani, Cavan, Monod and Bergez (submitted to Software Impacts).

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
