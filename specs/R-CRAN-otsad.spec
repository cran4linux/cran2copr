%global packname  otsad
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Online Time Series Anomaly Detectors

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-sigmoid 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-sigmoid 
Requires:         R-CRAN-reticulate 

%description
Implements a set of online fault detectors for time-series, called: PEWMA
see M. Carter et al. (2012) <doi:10.1109/SSP.2012.6319708>, SD-EWMA and
TSSD-EWMA see H. Raza et al. (2015) <doi:10.1016/j.patcog.2014.07.028>,
KNN-CAD see E. Burnaev et al. (2016) <arXiv:1608.04585>, KNN-LDCD see V.
Ishimtsev et al. (2017) <arXiv:1706.03412> and CAD-OSE see M. Smirnov
(2018) <https://github.com/smirmik/CAD>. The first three algorithms belong
to prediction-based techniques and the last three belong to window-based
techniques. In addition, the SD-EWMA and PEWMA algorithms are algorithms
designed to work in stationary environments, while the other four are
algorithms designed to work in non-stationary environments.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/python
%{rlibdir}/%{packname}/INDEX
