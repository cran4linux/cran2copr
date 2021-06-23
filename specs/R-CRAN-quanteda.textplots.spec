%global __brp_check_rpaths %{nil}
%global packname  quanteda.textplots
%global packver   0.94
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.94
Release:          1%{?dist}%{?buildtag}
Summary:          Plots for the Quantitative Analysis of Textual Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-grid 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-network 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-stringi 

%description
Plotting functions for visualising textual data.  Extends 'quanteda' and
related packages with plot methods designed specifically for text data,
textual statistics, and models fit to textual data. Plot types include
word clouds, lexical dispersion plots, scaling plots, network
visualisations, and word 'keyness' plots.

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
