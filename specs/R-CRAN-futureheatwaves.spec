%global packname  futureheatwaves
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Find, Characterize, and Explore Extreme Events in ClimateProjections

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ggthemes >= 3.0.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-data.table >= 1.10.0
BuildRequires:    R-CRAN-stringr >= 1.1.0
BuildRequires:    R-CRAN-leaflet >= 1.0.1
BuildRequires:    R-CRAN-tidyr >= 0.6.0
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-ggthemes >= 3.0.0
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-data.table >= 1.10.0
Requires:         R-CRAN-stringr >= 1.1.0
Requires:         R-CRAN-leaflet >= 1.0.1
Requires:         R-CRAN-tidyr >= 0.6.0
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-Rcpp >= 0.12.5

%description
Inputs a directory of climate projection files and, for each, identifies
and characterizes heat waves for specified study locations. The definition
used to identify heat waves can be customized. Heat wave characterizations
include several metrics of heat wave length, intensity, and timing in the
year. The heat waves that are identified can be explored using a function
to apply user-created functions across all generated heat wave files.This
work was supported in part by grants from the National Institute of
Environmental Health Sciences (R00ES022631), the National Science
Foundation (1331399), and the Colorado State University Vice President for
Research.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
