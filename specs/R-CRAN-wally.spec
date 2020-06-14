%global packname  wally
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          2%{?dist}
Summary:          The Wally Calibration Plot for Risk Prediction Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildArch:        noarch
BuildRequires:    R-CRAN-prodlim >= 1.4.9
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-riskRegression >= 1.0.8
BuildRequires:    R-stats 
Requires:         R-CRAN-prodlim >= 1.4.9
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-riskRegression >= 1.0.8
Requires:         R-stats 

%description
A prediction model is calibrated if, roughly, for any percentage x we can
expect that x subjects out of 100 experience the event among all subjects
that have a predicted risk of x%. A calibration plot provides a simple,
yet useful, way of assessing the calibration assumption. The Wally plot
consists of a sequence of usual calibration plots. Among the plots
contained within the sequence, one is the actual calibration plot which
has been obtained from the data and the others are obtained from similar
simulated data under the calibration assumption. It provides the
investigator with a direct visual understanding of the shape and sampling
variability that are common under the calibration assumption. The original
calibration plot from the data is included randomly among the simulated
calibration plots, similarly to a police lineup. If the original
calibration plot is not easily identified then the calibration assumption
is not contradicted by the data. The method handles the common situations
in which the data contain censored observations and occurrences of
competing events.

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
%{rlibdir}/%{packname}/INDEX
