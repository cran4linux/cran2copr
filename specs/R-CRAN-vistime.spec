%global packname  vistime
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pretty Timelines

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.0.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-ggrepel >= 0.7.0
BuildRequires:    R-CRAN-RColorBrewer >= 0.2.2
BuildRequires:    R-CRAN-assertive.types >= 0.0.3
Requires:         R-CRAN-plotly >= 4.0.0
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-ggrepel >= 0.7.0
Requires:         R-CRAN-RColorBrewer >= 0.2.2
Requires:         R-CRAN-assertive.types >= 0.0.3

%description
A library for creating time based charts, like Gantt or timelines.
Possible outputs include 'ggplot' diagrams, 'Plotly' graphs, 'Highchart'
widgets and 'data.frames'. Results can be used in the 'RStudio' viewer
pane, in 'RMarkdown' documents or in 'Shiny' apps. In the interactive
outputs created by 'vistime()' and 'hc_vistime()', you can interact with
the plot using mouse hover or zoom.

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
