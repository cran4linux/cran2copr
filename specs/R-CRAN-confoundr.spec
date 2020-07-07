%global packname  confoundr
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Diagnostics for Confounding of Time-Varying and Other JointExposures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-Rmpfr >= 0.7.0
BuildRequires:    R-CRAN-scales >= 0.5.0
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-rlang >= 0.2.1
BuildRequires:    R-grid 
BuildRequires:    R-stats 
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-Rmpfr >= 0.7.0
Requires:         R-CRAN-scales >= 0.5.0
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-rlang >= 0.2.1
Requires:         R-grid 
Requires:         R-stats 

%description
Implements three covariate-balance diagnostics for time-varying
confounding and selection-bias in complex longitudinal data, as described
in Jackson (2016) <doi:10.1097/EDE.0000000000000547> and Jackson (2019)
<doi:10.1093/aje/kwz136>. Diagnostic 1 assesses measured
confounding/selection-bias, diagnostic 2 assesses exposure-covariate
feedback, and diagnostic 3 assesses residual confounding/selection-bias
after inverse probability weighting or propensity score stratification.
All diagnostics appropriately account for exposure history, can be adapted
to assess a particular depth of covariate history, and can be implemented
in right-censored data. Balance assessments can be obtained for all times,
selected-times, or averaged across person-time. The balance measures are
reported as tables or plots. These diagnostics can be applied to the study
of multivariate exposures including time-varying exposures, direct
effects, interaction, and censoring.

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
%doc %{rlibdir}/%{packname}/AUTHOR
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/SoftwareManual_R_1_1.pdf
%{rlibdir}/%{packname}/INDEX
