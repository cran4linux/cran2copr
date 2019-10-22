%global packname  npregfast
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}
Summary:          Nonparametric Estimation of Regression Models withFactor-by-Curve Interactions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-wesanderson 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-mgcv 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-wesanderson 
Requires:         R-CRAN-ggplot2 

%description
A method for obtaining nonparametric estimates of regression models with
or without factor-by-curve interactions using local polynomial kernel
smoothers or splines. Additionally, a parametric model (allometric model)
can be estimated.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/shiny_examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
