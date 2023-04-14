%global __brp_check_rpaths %{nil}
%global packname  egg
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          3%{?dist}%{?buildtag}
Summary:          Extensions for 'ggplot2': Custom Geom, Custom Themes, PlotAlignment, Labelled Panels, Symmetric Scales, and Fixed PanelSize

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtable 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Miscellaneous functions to help customise 'ggplot2' objects. High-level
functions are provided to post-process 'ggplot2' layouts and allow
alignment between plot panels, as well as setting panel sizes to fixed
values. Other functions include a custom 'geom', and helper functions to
enforce symmetric scales or add tags to facetted plots.

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
