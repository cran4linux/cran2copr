%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  toxEval
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Exploring Biological Relevance of Environmental Chemistry Observations

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-leaflet >= 1.0.0
BuildRequires:    R-CRAN-DT >= 0.1.24
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-leaflet >= 1.0.0
Requires:         R-CRAN-DT >= 0.1.24
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-readxl 
Requires:         R-tools 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-utils 

%description
Data analysis package for estimating potential biological effects from
chemical concentrations in environmental samples. Included are a set of
functions to analyze, visualize, and organize measured concentration data
as it relates to user-selected chemical-biological interaction benchmark
data such as water quality criteria. The intent of these analyses is to
develop a better understanding of the potential biological relevance of
environmental chemistry data. Results can be used to prioritize which
chemicals at which sites may be of greatest concern. These methods are
meant to be used as a screening technique to predict potential for
biological influence from chemicals that ultimately need to be validated
with direct biological assays. A description of the analysis can be found
in Blackwell (2017) <doi:10.1021/acs.est.7b01613>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
