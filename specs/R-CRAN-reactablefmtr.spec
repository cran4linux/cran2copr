%global __brp_check_rpaths %{nil}
%global packname  reactablefmtr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Streamlined Table Styling and Formatting for Reactable

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 1.5.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-sass >= 0.4.0
BuildRequires:    R-CRAN-reactable >= 0.2.0
BuildRequires:    R-CRAN-tippy >= 0.1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-webshot 
Requires:         R-CRAN-htmlwidgets >= 1.5.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-sass >= 0.4.0
Requires:         R-CRAN-reactable >= 0.2.0
Requires:         R-CRAN-tippy >= 0.1.0
Requires:         R-CRAN-dplyr 
Requires:         R-grDevices 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-webshot 

%description
Provides various features to streamline and enhance the styling of
interactive reactable tables with easy-to-use and highly-customizable
functions and themes. Apply conditional formatting to cells with data
bars, color scales, color tiles, and icon sets. Utilize custom table
themes inspired by popular websites such and bootstrap themes. Apply
sparkline line & bar charts (note this feature requires the 'dataui'
package which can be downloaded from
<https://github.com/timelyportfolio/dataui>). Increase the portability and
reproducibility of reactable tables by embedding images from the web
directly into cells. Save the final table output as a static image or
interactive file.

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
