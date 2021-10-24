%global __brp_check_rpaths %{nil}
%global packname  easylabel
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Scatter Plot and Volcano Plot Labels

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.10.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-splus2R 
Requires:         R-CRAN-plotly >= 4.10.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-splus2R 

%description
Interactive labelling of scatter plots, volcano plots and Manhattan plots
using a 'shiny' and 'plotly' interface. Users can hover over points to see
where specific points are located and click points on/off to easily label
them. Labels can be dragged around the plot to place them optimally. Plots
can be exported directly to PDF for publication.

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
