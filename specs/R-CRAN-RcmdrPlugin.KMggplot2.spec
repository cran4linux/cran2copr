%global packname  RcmdrPlugin.KMggplot2
%global packver   0.2-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          2%{?dist}
Summary:          R Commander Plug-in for Data Visualization with 'ggplot2'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggthemes >= 4.2.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-Rcmdr >= 2.6.0
BuildRequires:    R-survival >= 2.44.1.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-tcltk2 >= 1.2.11
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-ggthemes >= 4.2.0
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-Rcmdr >= 2.6.0
Requires:         R-survival >= 2.44.1.1
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-tcltk2 >= 1.2.11
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
A GUI front-end for 'ggplot2' supports Kaplan-Meier plot, histogram, Q-Q
plot, box plot, errorbar plot, scatter plot, line chart, pie chart, bar
chart, contour plot, and distribution plot.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
