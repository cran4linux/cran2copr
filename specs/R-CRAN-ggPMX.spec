%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggPMX
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          'ggplot2' Based Tool to Facilitate Diagnostic Plots for NLME Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-scales 

%description
At Novartis, we aimed at standardizing the set of diagnostic plots used
for modeling activities in order to reduce the overall effort required for
generating such plots. For this, we developed a guidance that proposes an
adequate set of diagnostics and a toolbox, called 'ggPMX' to execute them.
'ggPMX' is a toolbox that can generate all diagnostic plots at a quality
sufficient for publication and submissions using few lines of code. This
package focuses on plots recommended by ISoP <doi:10.1002/psp4.12161>.
While not required, you can get/install the 'R' 'lixoftConnectors' package
in the 'Monolix' installation, as described at the following url
<https://monolixsuite.slp-software.com/r-functions/2024R1/installation-and-initialization>.
When 'lixoftConnectors' is available, 'R' can use 'Monolix' directly to
create the required Chart Data instead of exporting it from the 'Monolix'
gui.

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
