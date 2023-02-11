%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sherlock
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Displays to Aid Structured Problem Solving and Diagnosis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggh4x 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rstudioapi 

%description
Powerful graphical displays and statistical tools for structured problem
solving and diagnosis. The functions of the 'sherlock' package are
especially useful for applying the process of elimination as a problem
diagnosis technique. The 'sherlock' package was designed to seamlessly
work with the 'tidyverse' set of packages and provides a collection of
graphical displays built on top of the 'ggplot' and 'plotly' packages,
such as different kinds of small multiple plots as well as helper
functions such as adding reference lines, normalizing observations,
reading in data or saving analysis results in an Excel file. References:
David Hartshorne (2019, ISBN: 978-1-5272-5139-7). Stefan H. Steiner, R.
Jock MacKay (2005, ISBN: 0873896467).

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
