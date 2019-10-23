%global packname  VRPM
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Visualizing Risk Prediction Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-R2HTML 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-Hmisc 
Requires:         R-survival 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-R2HTML 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 

%description
This is a package to visualize risk prediction models. For each predictor,
a color bar represents the contribution to the linear predictor or latent
variable. A conversion from the linear predictor to the estimated risk or
survival is also given. (Cumulative) contribution charts enable to
visualize how the estimated risk for one particular observation is
obtained by the model. Several options allow to choose different color
maps, and to select the zero level of the contributions. The package is
able to deal with 'glm', 'coxph', 'mfp', 'multinom' and 'ksvm' objects.
For 'ksvm' objects, the visualization is not always exact. Functions
providing tools to indicate the accuracy of the approximation are provided
in addition to the visualization.

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
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
