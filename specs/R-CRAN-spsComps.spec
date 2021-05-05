%global packname  spsComps
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          'systemPipeShiny' UI and Server Components

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-glue >= 1.4.0
BuildRequires:    R-CRAN-spsUtil 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-bsplus 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinytoastr 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-glue >= 1.4.0
Requires:         R-CRAN-spsUtil 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-bsplus 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinytoastr 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-crayon 

%description
The systemPipeShiny (SPS) framework comes with many UI and server
components. However, installing the whole framework is heavy and takes
some time. If you would like to use UI and server components from SPS in
your own Shiny apps, but do not want to install the whole framework, just
install this package.

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
