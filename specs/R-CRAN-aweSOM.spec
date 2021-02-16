%global packname  aweSOM
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Self-Organizing Maps

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-kohonen 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rclipboard 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-kohonen 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rclipboard 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-kernlab 
Requires:         R-stats 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-readxl 

%description
Self-organizing maps (also known as SOM, see Kohonen (2001)
<doi:10.1007/978-3-642-56927-2>) are a method for dimensionality reduction
and clustering of continuous data. This package introduces interactive
(html) graphics for easier analysis of SOM results. It also features an
interactive interface, for push-button training and visualization of SOM
on numeric, categorical or mixed data, as well as tools to evaluate the
quality of SOM.

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
