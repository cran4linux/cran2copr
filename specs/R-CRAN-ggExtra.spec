%global packname  ggExtra
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          1%{?dist}
Summary:          Add Marginal Histograms to 'ggplot2', and More 'ggplot2'Enhancements

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

Requires:         pandoc
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-grid >= 3.1.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-colourpicker >= 1.0
BuildRequires:    R-CRAN-shinyjs >= 0.5.2
BuildRequires:    R-CRAN-gtable >= 0.2.0
BuildRequires:    R-CRAN-scales >= 0.2.0
BuildRequires:    R-CRAN-shiny >= 0.13.0
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-grid >= 3.1.3
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-colourpicker >= 1.0
Requires:         R-CRAN-shinyjs >= 0.5.2
Requires:         R-CRAN-gtable >= 0.2.0
Requires:         R-CRAN-scales >= 0.2.0
Requires:         R-CRAN-shiny >= 0.13.0
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-grDevices 
Requires:         R-utils 

%description
Collection of functions and layers to enhance 'ggplot2'. The flagship
function is 'ggMarginal()', which can be used to add marginal
histograms/boxplots/density plots to 'ggplot2' scatterplots.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/gadgets
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/vignette_files
%{rlibdir}/%{packname}/INDEX
