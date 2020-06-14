%global packname  sbpiper
%global packver   1.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.0
Release:          2%{?dist}
Summary:          Data Analysis Functions for 'SBpipe' Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-FactoMineR 
Requires:         R-grDevices 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Provides an API for analysing repetitive parameter estimations and
simulations of mathematical models. Examples of mathematical models are
Ordinary Differential equations (ODEs) or Stochastic Differential
Equations (SDEs) models. Among the analyses for parameter estimation
'sbpiper' calculates statistics and generates plots for parameter density,
PCA of the best fits, parameter profile likelihood estimations (PLEs), and
2D parameter PLEs. These results can be generated using all or a subset of
the best computed parameter sets. Among the analyses for model simulation
'sbpiper' calculates statistics and generates plots for deterministic and
stochastic time courses via cartesian and heatmap plots. Plots for the
scan of one or two model parameters can also be generated. This package is
primarily used by the software 'SBpipe'. Citation: Dalle Pezze P, Le
Novère N. SBpipe: a collection of pipelines for automating repetitive
simulation and analysis tasks. BMC Systems Biology. 2017;11:46.
<doi:10.1186/s12918-017-0423-3>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
