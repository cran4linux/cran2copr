%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BlockmodelingGUI
%global packver   1.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.4
Release:          1%{?dist}%{?buildtag}
Summary:          GUI for the Generalised Blockmodeling of Valued Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-blockmodeling 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-intergraph 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-blockmodeling 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-intergraph 
Requires:         R-CRAN-network 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-visNetwork 

%description
This app provides some useful tools for Offering an accessible GUI for
generalised blockmodeling of single-relation, one-mode networks. The user
can execute blockmodeling without having to write a line code by using the
app's visual helps. Moreover, there are several ways to visualisations
networks and their partitions. Finally, the results can be exported as if
they were produced by writing code. The development of this package is
financially supported by the Slovenian Research Agency (www.arrs.gov.si)
within the research project J5-2557 (Comparison and evaluation of
different approaches to blockmodeling dynamic networks by simulations with
application to Slovenian co-authorship networks).

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
