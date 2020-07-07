%global packname  vistime
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Pretty Timelines

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.0.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-RColorBrewer >= 0.2.2
BuildRequires:    R-CRAN-assertive >= 0.1.4
Requires:         R-CRAN-plotly >= 4.0.0
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-RColorBrewer >= 0.2.2
Requires:         R-CRAN-assertive >= 0.1.4

%description
A library for creating time based charts, like Gantt or timelines.
Possible outputs include 'ggplot' diagrams, 'Plotly' graphs and
'data.frame's. Results can be used in the 'RStudio' viewer pane, in
'RMarkdown' documents or in 'Shiny' apps. In the interactive 'Plotly'
output, you can hover the mouse pointer over a point or task to show
details or drag a rectangle to zoom in.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/WORDLIST.R
%{rlibdir}/%{packname}/INDEX
