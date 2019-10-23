%global packname  DynNom
%global packver   5.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0.1
Release:          1%{?dist}
Summary:          Visualising Statistical Models using Dynamic Nomograms

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival >= 2.38.3
BuildRequires:    R-CRAN-ggplot2 > 2.1.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-stargazer 
BuildRequires:    R-CRAN-prediction 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-compare 
BuildRequires:    R-CRAN-BBmisc 
Requires:         R-survival >= 2.38.3
Requires:         R-CRAN-ggplot2 > 2.1.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-stargazer 
Requires:         R-CRAN-prediction 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-compare 
Requires:         R-CRAN-BBmisc 

%description
Demonstrate the results of a statistical model object as a dynamic
nomogram in an RStudio panel or web browser. The package provides two
generics functions: DynNom, which display statistical model objects as a
dynamic nomogram; DNbuilder, which builds required scripts to publish a
dynamic nomogram on a web server such as the <https://www.shinyapps.io/>.
Current version of 'DynNom' supports stats::lm, stats::glm,
survival::coxph, rms::ols, rms::Glm, rms::lrm, rms::cph, mgcv::gam and
gam::gam model objects.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
