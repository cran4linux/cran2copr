%global __brp_check_rpaths %{nil}
%global packname  nlrx
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Setup, Run and Analyze 'NetLogo' Model Simulations from 'R' via 'XML'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-sensitivity 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-genalg 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-EasyABC 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-sensitivity 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-genalg 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-EasyABC 

%description
Setup, run and analyze 'NetLogo' (<https://ccl.northwestern.edu/netlogo/>)
model simulations in 'R'. 'nlrx' experiments use a similar structure as
'NetLogos' Behavior Space experiments. However, 'nlrx' offers more
flexibility and additional tools for running and analyzing complex
simulation designs and sensitivity analyses. The user defines all
information that is needed in an intuitive framework, using class objects.
Experiments are submitted from 'R' to 'NetLogo' via 'XML' files that are
dynamically written, based on specifications defined by the user. By
nesting model calls in future environments, large simulation design with
many runs can be executed in parallel. This also enables simulating
'NetLogo' experiments on remote high performance computing machines. In
order to use this package, 'Java' and 'NetLogo' (>= 5.3.1) need to be
available on the executing system.

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
