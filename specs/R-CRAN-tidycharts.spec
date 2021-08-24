%global __brp_check_rpaths %{nil}
%global packname  tidycharts
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Tidy Charts Inspired by 'IBCS'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-rsvg 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-rsvg 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 

%description
There is a wide range of R packages created for data visualization, but
still, there was no simple and easily accessible way to create clean and
transparent charts - up to now. The 'tidycharts' package enables the user
to generate charts compliant with International Business Communication
Standards ('IBCS'). It means unified bar widths, colors, chart sizes, etc.
Creating homogeneous reports has never been that easy! Additionally, users
can apply semantic notation to indicate different data scenarios (plan,
budget, forecast). What's more, it is possible to customize the charts by
creating a personal color pallet with the possibility of switching to
default options after the experiments. We wanted the package to be helpful
in writing reports, so we also made joining charts in a one, clear image
possible. All charts are generated in SVG format and can be shown in the
'RStudio' viewer pane or exported to HTML output of 'knitr'/'markdown'.

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
