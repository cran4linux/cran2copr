%global packname  colourpicker
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          A Colour Picker Tool for Shiny and for Selecting Colours inPlots

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 0.7
BuildRequires:    R-CRAN-shiny >= 0.11.1
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-utils 
Requires:         R-CRAN-htmlwidgets >= 0.7
Requires:         R-CRAN-shiny >= 0.11.1
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-shinyjs 
Requires:         R-utils 

%description
A colour picker that can be used as an input in Shiny apps or Rmarkdown
documents. The colour picker supports alpha opacity, custom colour
palettes, and many more options. A Plot Colour Helper tool is available as
an RStudio Addin, which helps you pick colours to use in your plots. A
more generic Colour Picker RStudio Addin is also provided to let you
select colours to use in your R code.

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
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/srcjs
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
