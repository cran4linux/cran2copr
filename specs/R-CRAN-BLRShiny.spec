%global __brp_check_rpaths %{nil}
%global packname  BLRShiny
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Document for Working with Binary Logistic RegressionAnalysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-dplyr 
Requires:         R-datasets 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-ggplot2 

%description
An interactive document on the topic of binary logistic regression
analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are
provided in the package function as well as at
<https://analyticmodels.shinyapps.io/BinaryLogisticRegressionModelling/>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
