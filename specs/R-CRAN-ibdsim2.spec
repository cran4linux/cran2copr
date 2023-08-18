%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ibdsim2
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation of Chromosomal Regions Shared by Family Members

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-pedtools >= 2.2.0
BuildRequires:    R-CRAN-ribd >= 1.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-pedtools >= 2.2.0
Requires:         R-CRAN-ribd >= 1.5.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 

%description
Simulation of segments shared identical-by-descent (IBD) by pedigree
members. Using sex specific recombination rates along the human genome
(Halldorsson et al. (2019) <doi:10.1126/science.aau1043>), phased
chromosomes are simulated for all pedigree members. Applications include
calculation of realised relatedness coefficients and IBD segment
distributions. 'ibdsim2' is part of the 'ped suite' collection of packages
for pedigree analysis. A detailed presentation of the 'ped suite',
including a separate chapter on 'ibdsim2', is available in the book
'Pedigree analysis in R' (Vigeland, 2021, ISBN:9780128244302). A 'shiny'
app for visualising and comparing IBD distributions is available at
<https://magnusdv.shinyapps.io/ibdsim2-shiny/>.

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
