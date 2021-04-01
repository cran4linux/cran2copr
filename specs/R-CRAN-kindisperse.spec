%global packname  kindisperse
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate and Estimate Close-Kin Dispersal Kernels

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-here 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-grid 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-stringr 

%description
Functions for simulating and estimating kinship-related dispersal. Based
on the methods described in M. Jasper, T.L. Schmidt., N.W. Ahmad, S.P.
Sinkins & A.A. Hoffmann (2019) <doi:10.1111/1755-0998.13043> "A genomic
approach to inferring kinship reveals limited intergenerational dispersal
in the yellow fever mosquito". Assumes an additive variance model of
dispersal in two dimensions, compatible with Wright's neighbourhood area.
Simple and composite dispersal simulations are supplied, as well as the
functions needed to estimate parent-offspring dispersal for simulated or
empirical data, and to undertake sampling design for future field studies
of dispersal. For ease of use an integrated Shiny app is also included.

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
