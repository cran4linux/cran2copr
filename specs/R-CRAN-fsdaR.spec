%global packname  fsdaR
%global packver   0.4-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.9
Release:          2%{?dist}
Summary:          Robust Data Analysis Through Monitoring and DynamicVisualization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-rJava 
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-CRAN-ggplot2 

%description
Provides interface to the 'MATLAB' toolbox 'Flexible Statistical Data
Analysis (FSDA)' which is a comprehensive and computationally efficient
software package for robust statistics in regression, multivariate and
categorical data analysis. The current R version implements tools for
regression: (forward search, S- and MM-estimation, least trimmed squares
(LTS) and least median of squares (LMS)), for multivariate analysis
(forward search, S- and MM-estimation), for cluster analysis and
cluster-wise regression. The distinctive feature of our package is the
possibility of monitoring the statistics of interest as function of
breakdown point, efficiency or subset size, depending on the estimator.
This is accompanied by a rich set of graphical features, such as dynamic
brushing, linking, particularly useful for exploratory data analysis.

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
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/work
%{rlibdir}/%{packname}/INDEX
