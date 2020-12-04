%global packname  shinydlplot
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Add a Download Button to a 'shiny' Plot or 'plotly'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.2
BuildRequires:    R-CRAN-htmlwidgets >= 1.5.1
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-shinyjs >= 1.1
BuildRequires:    R-CRAN-shinyBS >= 0.61
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-plotly >= 4.9.2
Requires:         R-CRAN-htmlwidgets >= 1.5.1
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-shinyjs >= 1.1
Requires:         R-CRAN-shinyBS >= 0.61
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-methods 
Requires:         R-utils 

%description
Add a download button to a 'shiny' plot or 'plotly' that appears when the
plot is hovered. A tooltip, styled to resemble 'plotly' buttons, is
displayed on hover of the download button. The download button can be used
to allow users to download the dataset used for a plot.

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
