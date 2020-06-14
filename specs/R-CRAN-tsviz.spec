%global packname  tsviz
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Easy and Interactive Time Series Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.7
BuildRequires:    R-CRAN-plotly >= 4.9
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-lubridate >= 1.7
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.2
BuildRequires:    R-CRAN-dplyr >= 0.8
BuildRequires:    R-CRAN-shinyhelper >= 0.3.1
BuildRequires:    R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-forecast >= 8.7
Requires:         R-CRAN-plotly >= 4.9
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-lubridate >= 1.7
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-shiny >= 1.2
Requires:         R-CRAN-dplyr >= 0.8
Requires:         R-CRAN-shinyhelper >= 0.3.1
Requires:         R-CRAN-miniUI >= 0.1.1

%description
An 'RStudio' add-in to visualize time series. Time series are searched in
the global environment as data.frame objects with a column of type date
and a column of type numeric. Interactive charts are produced using
'plotly' package.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
