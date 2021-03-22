%global packname  CaPO4Sim
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Virtual Patient Simulator in the Context of Calcium and Phosphate Homeostasis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-shinyjqui 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-shinyjqui 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 

%description
Explore calcium (Ca) and phosphate (Pi) homeostasis with two novel 'Shiny'
apps, building upon on a previously published mathematical model written
in C, to ensure efficient computations. The underlying model is accessible
here <https://pubmed.ncbi.nlm.nih.gov/28747359/)>. The first application
explores the fundamentals of Ca-Pi homeostasis, while the second provides
interactive case studies for in-depth exploration of the topic, thereby
seeking to foster student engagement and an integrative understanding of
Ca-Pi regulation. These applications are hosted at
<https://rinterface.com/AppsPhysiol.html>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
