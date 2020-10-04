%global packname  SSDM
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          3%{?dist}%{?buildtag}
Summary:          Stacked Species Distribution Modelling

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-nnet >= 7.3.10
BuildRequires:    R-CRAN-randomForest >= 4.6.10
BuildRequires:    R-CRAN-earth >= 4.4.3
BuildRequires:    R-rpart >= 4.1.10
BuildRequires:    R-methods >= 3.2.2
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-raster >= 2.9.5
BuildRequires:    R-CRAN-gbm >= 2.1.1
BuildRequires:    R-mgcv >= 1.8.7
BuildRequires:    R-CRAN-e1071 >= 1.6.7
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-poibin >= 1.3
BuildRequires:    R-CRAN-sp >= 1.2.0
BuildRequires:    R-CRAN-dismo >= 1.0.12
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-shinyFiles >= 0.7.0
BuildRequires:    R-CRAN-shinydashboard >= 0.5.1
BuildRequires:    R-CRAN-shiny >= 0.12.2
BuildRequires:    R-CRAN-spThin >= 0.1.0
Requires:         R-nnet >= 7.3.10
Requires:         R-CRAN-randomForest >= 4.6.10
Requires:         R-CRAN-earth >= 4.4.3
Requires:         R-rpart >= 4.1.10
Requires:         R-methods >= 3.2.2
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-raster >= 2.9.5
Requires:         R-CRAN-gbm >= 2.1.1
Requires:         R-mgcv >= 1.8.7
Requires:         R-CRAN-e1071 >= 1.6.7
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-poibin >= 1.3
Requires:         R-CRAN-sp >= 1.2.0
Requires:         R-CRAN-dismo >= 1.0.12
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-shinyFiles >= 0.7.0
Requires:         R-CRAN-shinydashboard >= 0.5.1
Requires:         R-CRAN-shiny >= 0.12.2
Requires:         R-CRAN-spThin >= 0.1.0

%description
Allows to map species richness and endemism based on stacked species
distribution models (SSDM). Individuals SDMs can be created using a single
or multiple algorithms (ensemble SDMs). For each species, an SDM can yield
a habitat suitability map, a binary map, a between-algorithm variance map,
and can assess variable importance, algorithm accuracy, and between-
algorithm correlation. Methods to stack individual SDMs include summing
individual probabilities and thresholding then summing. Thresholding can
be based on a specific evaluation metric or by drawing repeatedly from a
Bernoulli distribution. The SSDM package also provides a user-friendly
interface.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
