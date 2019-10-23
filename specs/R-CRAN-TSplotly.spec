%global packname  TSplotly
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Create Interactive Plots on Time Series Dataset

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dcemriS4 
BuildRequires:    R-CRAN-prettydoc 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dcemriS4 
Requires:         R-CRAN-prettydoc 

%description
To better visualize time-series dataset, 'TSplotly' package provides an
effective mechanism to utilize the powerful 'plotly' package for graphing
time series data. It contains 5 core functions: TSplot(): create
interactive plot on time series data or fitted ARIMA(X) models. ADDline():
add lines on existing 'TSplot()' objects, as needed. GGtoPY(): create a
convenient way to transform (reformat) 'ggplot2' datasets into a format
that can work on 'plot_ly()'. GTSplot(): create multiple 'plot_ly()' lines
(time-series) based on data frames containing multiple time-series data.
TSplot_gen(): a more general version of function 'TSplot()' that can work
on any time format.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
