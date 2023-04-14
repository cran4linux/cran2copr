%global __brp_check_rpaths %{nil}
%global packname  metricsgraphics
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          3%{?dist}%{?buildtag}
Summary:          Create Interactive Charts with the JavaScript 'MetricsGraphics'Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 

%description
Provides an 'htmlwidgets' interface to the 'MetricsGraphics.js'
('D3'-based) charting library which is geared towards displaying
time-series data. Chart types include line charts, scatterplots,
histograms and rudimentary bar charts. Support for laying out multiple
charts into a grid layout is also provided. All charts are interactive and
many have an option for line, label and region annotations.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
