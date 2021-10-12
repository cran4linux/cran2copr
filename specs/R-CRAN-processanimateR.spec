%global __brp_check_rpaths %{nil}
%global packname  processanimateR
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Process Map Token Replay Animation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.0
BuildRequires:    R-CRAN-processmapR >= 0.3.1
BuildRequires:    R-CRAN-bupaR 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-DiagrammeR >= 1.0.0
Requires:         R-CRAN-processmapR >= 0.3.1
Requires:         R-CRAN-bupaR 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-grDevices 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-htmltools 

%description
Provides animated process maps based on the 'procesmapR' package. Cases
stored in event logs created with with 'bupaR' S3 class eventlog() are
rendered as tokens (SVG shapes) and animated according to their occurrence
times on top of the process map. For rendering SVG animations ('SMIL') and
the 'htmlwidget' package are used.

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
