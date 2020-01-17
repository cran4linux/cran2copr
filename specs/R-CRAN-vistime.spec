%global packname  vistime
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Pretty Timeline Creation

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.0.0
BuildRequires:    R-CRAN-RColorBrewer >= 0.2.2
BuildRequires:    R-CRAN-assertive >= 0.1.4
Requires:         R-CRAN-plotly >= 4.0.0
Requires:         R-CRAN-RColorBrewer >= 0.2.2
Requires:         R-CRAN-assertive >= 0.1.4

%description
Create interactive timelines or Gantt charts that are usable in the
'RStudio' viewer pane, in 'R Markdown' documents and in 'Shiny' apps.
Hover the mouse pointer over a point or task to show details or drag a
rectangle to zoom in. Timelines and their components can afterwards be
manipulated using plotly_build(), which transforms the plot into a mutable
list.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/INDEX
