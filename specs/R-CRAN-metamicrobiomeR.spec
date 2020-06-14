%global packname  metamicrobiomeR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Analysis of Microbiome Relative Abundance Data using ZeroInflated Beta GAMLSS and Meta-Analysis Across Studies usingRandom Effects Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-tools 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-zCompositions 
BuildRequires:    R-CRAN-compositions 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-repmis 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-meta 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-lmerTest 
Requires:         R-mgcv 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-randomForest 
Requires:         R-grDevices 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-magrittr 
Requires:         R-tools 
Requires:         R-foreign 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-zCompositions 
Requires:         R-CRAN-compositions 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-repmis 
Requires:         R-CRAN-jsonlite 

%description
Generalized Additive Model for Location, Scale and Shape (GAMLSS) with
zero inflated beta (BEZI) family for analysis of microbiome relative
abundance data (with various options for data transformation/normalization
to address compositional effects) and random effects meta-analysis models
for meta-analysis pooling estimates across microbiome studies are
implemented. Random Forest model to predict microbiome age based on
relative abundances of shared bacterial genera with the Bangladesh data
(Subramanian et al 2014), comparison of multiple diversity indexes using
linear/linear mixed effect models and some data display/visualization are
also implemented. The reference paper is published by Ho NT, Li F, Wang S,
Kuhn L (2019) <doi:10.1186/s12859-019-2744-2> .

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
