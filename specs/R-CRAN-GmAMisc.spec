%global packname  GmAMisc
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Gianmarco Alberti Miscellaneous

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.1.1
BuildRequires:    R-graphics >= 3.4.3
BuildRequires:    R-grDevices >= 3.4.3
BuildRequires:    R-methods >= 3.4.3
BuildRequires:    R-stats >= 3.4.3
BuildRequires:    R-utils >= 3.4.3
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-cluster >= 2.0.7.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-spatstat >= 1.56.0
BuildRequires:    R-CRAN-shape >= 1.4.4
BuildRequires:    R-CRAN-rworldmap >= 1.3.6
BuildRequires:    R-CRAN-rgdal >= 1.3.3
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-coin >= 1.2.2
BuildRequires:    R-CRAN-caTools >= 1.17.1
BuildRequires:    R-CRAN-pROC >= 1.12.1
BuildRequires:    R-CRAN-dismo >= 1.1.4
BuildRequires:    R-CRAN-spatialEco >= 1.1.0
BuildRequires:    R-CRAN-RcmdrMisc >= 1.0.10
BuildRequires:    R-CRAN-DescTools >= 0.99.24
BuildRequires:    R-CRAN-maptools >= 0.9.2
BuildRequires:    R-CRAN-corrplot >= 0.84
BuildRequires:    R-CRAN-ggrepel >= 0.8.0
BuildRequires:    R-CRAN-lsr >= 0.5
BuildRequires:    R-CRAN-kimisc >= 0.4
BuildRequires:    R-CRAN-rgeos >= 0.3.28
BuildRequires:    R-CRAN-classInt >= 0.2.3
BuildRequires:    R-CRAN-InPosition >= 0.12.7
Requires:         R-CRAN-Hmisc >= 4.1.1
Requires:         R-graphics >= 3.4.3
Requires:         R-grDevices >= 3.4.3
Requires:         R-methods >= 3.4.3
Requires:         R-stats >= 3.4.3
Requires:         R-utils >= 3.4.3
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-cluster >= 2.0.7.1
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-spatstat >= 1.56.0
Requires:         R-CRAN-shape >= 1.4.4
Requires:         R-CRAN-rworldmap >= 1.3.6
Requires:         R-CRAN-rgdal >= 1.3.3
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-coin >= 1.2.2
Requires:         R-CRAN-caTools >= 1.17.1
Requires:         R-CRAN-pROC >= 1.12.1
Requires:         R-CRAN-dismo >= 1.1.4
Requires:         R-CRAN-spatialEco >= 1.1.0
Requires:         R-CRAN-RcmdrMisc >= 1.0.10
Requires:         R-CRAN-DescTools >= 0.99.24
Requires:         R-CRAN-maptools >= 0.9.2
Requires:         R-CRAN-corrplot >= 0.84
Requires:         R-CRAN-ggrepel >= 0.8.0
Requires:         R-CRAN-lsr >= 0.5
Requires:         R-CRAN-kimisc >= 0.4
Requires:         R-CRAN-rgeos >= 0.3.28
Requires:         R-CRAN-classInt >= 0.2.3
Requires:         R-CRAN-InPosition >= 0.12.7

%description
Contains many functions useful for univariate outlier detection,
permutation-based t-test, permutation-based chi-square test, visualization
of residuals, and bootstrap Cramer's V, plotting of the results of the
Mann-Whitney and Kruskall-Wallis test, calculation of Brainerd-Robinson
similarity coefficient and subsequent clustering, validation of logistic
regression models, optimism-corrected AUC, robust Bland-Altman plot,
calculation of posterior probability for different chronological
relationships between two Bayesian radiocarbon phases, point pattern
analysis, landform classification, clustering of spatial features.

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
