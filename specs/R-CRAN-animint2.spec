%global packname  animint2
%global packver   2019.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.7.3
Release:          1%{?dist}
Summary:          Animated Interactive Grammar of Graphics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.7.1
BuildRequires:    R-CRAN-scales >= 0.4.1
BuildRequires:    R-CRAN-gtable >= 0.1.1
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-grid 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lazyeval 
Requires:         R-CRAN-plyr >= 1.7.1
Requires:         R-CRAN-scales >= 0.4.1
Requires:         R-CRAN-gtable >= 0.1.1
Requires:         R-CRAN-digest 
Requires:         R-CRAN-RJSONIO 
Requires:         R-grid 
Requires:         R-MASS 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lazyeval 

%description
Functions are provided for defining animated, interactive data
visualizations in R code, and rendering on a web page. The 2018 Journal of
Computational and Graphical Statistics paper,
<doi:10.1080/10618600.2018.1513367> describes the concepts implemented.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/htmljs
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
