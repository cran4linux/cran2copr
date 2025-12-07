%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blockr.core
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Web-Framework for Data Manipulation and Visualization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-bsicons 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-DT 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-bsicons 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 

%description
A framework for data manipulation and visualization using a web-based
point and click user interface where analysis pipelines are decomposed
into re-usable and parameterizable blocks.

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
