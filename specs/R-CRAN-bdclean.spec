%global __brp_check_rpaths %{nil}
%global packname  bdclean
%global packver   0.1.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.15
Release:          3%{?dist}%{?buildtag}
Summary:          A User-Friendly Biodiversity Data Cleaning App for theInexperienced R User

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-spocc 
BuildRequires:    R-CRAN-finch 
BuildRequires:    R-CRAN-bdDwC 
BuildRequires:    R-CRAN-bdchecks 
BuildRequires:    R-methods 
BuildRequires:    R-tools 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-spocc 
Requires:         R-CRAN-finch 
Requires:         R-CRAN-bdDwC 
Requires:         R-CRAN-bdchecks 
Requires:         R-methods 
Requires:         R-tools 

%description
Provides features to manage the complete workflow for biodiversity data
cleaning. Uploading data, gathering input from users (in order to adjust
cleaning procedures), cleaning data and finally, generating various
reports and several versions of the data. Facilitates user-level data
cleaning, designed for the inexperienced R user. T Gueta et al (2018)
<doi:10.3897/biss.2.25564>. T Gueta et al (2017)
<doi:10.3897/tdwgproceedings.1.20311>.

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
%doc %{rlibdir}/%{packname}/rmd
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/txts
%{rlibdir}/%{packname}/INDEX
