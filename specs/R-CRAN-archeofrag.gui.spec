%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  archeofrag.gui
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Analysis in Archaeology from Refitting Fragments (GUI)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-archeofrag 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
Requires:         R-CRAN-archeofrag 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 

%description
A 'Shiny' application to access the functionalities and datasets of the
'archeofrag' package for spatial analysis in archaeology from refitting
data. Quick and seamless exploration of archaeological refitting datasets,
focusing on physical refits only. Features include: built-in documentation
and convenient workflow, plot generation and exports, anomaly detection in
the spatial distribution of refitting connection, exploration of spatial
units merging solutions, simulation of archaeological site formation
processes, support for parallel computing, R code generation to re-execute
simulations and ensure reproducibility, code generation for the 'openMOLE'
model exploration software. A demonstration of the app is available at
<https://analytics.huma-num.fr/Sebastien.Plutniak/archeofrag/>.

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
