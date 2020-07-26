%global packname  vistime
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
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
BuildRequires:    R-CRAN-assertthat >= 0.1
BuildRequires:    R-CRAN-highcharter > 0.1.0
Requires:         R-CRAN-plotly >= 4.0.0
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-ggrepel >= 0.7.0
Requires:         R-CRAN-RColorBrewer >= 0.2.2
Requires:         R-CRAN-assertthat >= 0.1
Requires:         R-CRAN-highcharter > 0.1.0

%description
A library for creating time based charts, like Gantt or timelines.
Possible outputs include 'ggplot' diagrams, 'Plotly' graphs, 'Highchart'
widgets and 'data.frames'. Results can be used in the 'RStudio' viewer
pane, in 'RMarkdown' documents or in 'Shiny' apps. In the interactive
outputs created by 'Plotly.js' and 'Highcharts.js', you can interact with
the plot using mouse hover or zoom.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
