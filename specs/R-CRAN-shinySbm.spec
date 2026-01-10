%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinySbm
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          'shiny' Application to Use the Stochastic Block Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.2
BuildRequires:    R-CRAN-golem >= 0.3.5
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-sbm 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-fresh 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-shiny >= 1.7.2
Requires:         R-CRAN-golem >= 0.3.5
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-sbm 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-fresh 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-parallel 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-shinydashboard 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-visNetwork 

%description
A 'shiny' interface for a simpler use of the 'sbm' R package. It also
contains useful functions to easily explore the 'sbm' package results.
With this package you should be able to use the stochastic block model
without any knowledge in R, get automatic reports and nice visuals, as
well as learning the basic functions of 'sbm'.

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
