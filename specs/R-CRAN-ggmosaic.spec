%global packname  ggmosaic
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Mosaic Plots in the 'ggplot2' Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.5.5
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-productplots >= 0.1.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-plotly >= 4.5.5
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-productplots >= 0.1.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
Mosaic plots in the 'ggplot2' framework. Mosaic plot functionality is
provided in a single 'ggplot2' layer by calling the geom 'mosaic'.

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
%doc %{rlibdir}/%{packname}/comparisons-vcd.R
%doc %{rlibdir}/%{packname}/comparisons.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example-not-working.R
%{rlibdir}/%{packname}/flydata.R
%doc %{rlibdir}/%{packname}/mosaic-rects.csv
%doc %{rlibdir}/%{packname}/nhanes.R
%doc %{rlibdir}/%{packname}/plotly-shiny
%doc %{rlibdir}/%{packname}/server.R
%doc %{rlibdir}/%{packname}/ui.R
%doc %{rlibdir}/%{packname}/vtest.R
%{rlibdir}/%{packname}/INDEX
