%global packname  tsfgrnn
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Time Series Forecasting Using GRNN

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
A general regression neural network (GRNN) is a variant of a Radial Basis
Function Network characterized by a fast single-pass learning. 'tsfgrnn'
allows you to forecast time series using a GRNN model Francisco Martinez
et al. (2019) <doi:10.1007/978-3-030-20521-8_17> and Weizhong Yan (2012)
<doi:10.1109/TNNLS.2012.2198074>. When the forecasting horizon is higher
than 1, two multi-step ahead forecasting strategies can be used. The model
built is autoregressive, that is, it is only based on the observations of
the time series. You can consult and plot how the prediction was done. It
is also possible to assess the forecasting accuracy of the model using
rolling origin evaluation.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
