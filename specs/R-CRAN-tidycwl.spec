%global packname  tidycwl
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Common Workflow Language Tools and Workflows

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-webshot 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-webshot 

%description
The Common Workflow Language <https://www.commonwl.org/> is an open
standard for describing data analysis workflows. This package takes the
raw Common Workflow Language workflows encoded in JSON or 'YAML' and turns
the workflow elements into tidy data frames or lists. A graph
representation for the workflow can be constructed and visualized with the
parsed workflow inputs, outputs, and steps. Users can embed the
visualizations in their 'Shiny' applications, and export them as HTML
files or static images.

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
