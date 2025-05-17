%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  apisensr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'episensr' for Sensitivity Analysis of Epidemiological Results

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-episensr >= 2.0.0
BuildRequires:    R-CRAN-attempt 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinymaterial 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-episensr >= 2.0.0
Requires:         R-CRAN-attempt 
Requires:         R-CRAN-config 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinymaterial 

%description
API for using 'episensr', Basic sensitivity analysis of the observed
relative risks adjusting for unmeasured confounding and misclassification
of the exposure/outcome, or both. See
<https://cran.r-project.org/package=episensr>.

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
