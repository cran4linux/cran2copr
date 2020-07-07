%global packname  mvMonitoring
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Multi-State Adaptive Dynamic Principal Component Analysis forMultivariate Process Monitoring

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-BMS 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-graphics 
Requires:         R-CRAN-BMS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-robustbase 
Requires:         R-graphics 

%description
Use multi-state splitting to apply Adaptive-Dynamic PCA (ADPCA) to data
generated from a continuous-time multivariate industrial or natural
process. Employ PCA-based dimension reduction to extract linear
combinations of relevant features, reducing computational burdens. For a
description of ADPCA, see <doi:10.1007/s00477-016-1246-2>, the 2016 paper
from Kazor et al. The multi-state application of ADPCA is from a
manuscript under current revision entitled "Multi-State Multivariate
Statistical Process Control" by Odom, Newhart, Cath, and Hering, and is
expected to appear in Q1 of 2018.

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
%doc %{rlibdir}/%{packname}/acf_lag_checks.R
%doc %{rlibdir}/%{packname}/bug_example_20170127.R
%doc %{rlibdir}/%{packname}/currentDayData_v2.csv
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/Functions_v0.R
%doc %{rlibdir}/%{packname}/Monitor_NOC_v0.R
%doc %{rlibdir}/%{packname}/mspGraphsGrid.R
%doc %{rlibdir}/%{packname}/mspSummary.R
%doc %{rlibdir}/%{packname}/Multi-State_AD-PCA_Sim_051216.R
%doc %{rlibdir}/%{packname}/mvMonitoring_20170131.pdf
%doc %{rlibdir}/%{packname}/NOC_Analysis.R
%doc %{rlibdir}/%{packname}/pH_Fault_Analysis.R
%doc %{rlibdir}/%{packname}/pH_Fault_Interpolation.R
%doc %{rlibdir}/%{packname}/R_to_Text_Playground.R
%doc %{rlibdir}/%{packname}/Simulation_Vignette.html
%doc %{rlibdir}/%{packname}/Simulation_Vignette.R
%doc %{rlibdir}/%{packname}/Simulation_Vignette.Rmd
%doc %{rlibdir}/%{packname}/tenDayData_v2.csv
%doc %{rlibdir}/%{packname}/testDataGeneration.R
%{rlibdir}/%{packname}/INDEX
