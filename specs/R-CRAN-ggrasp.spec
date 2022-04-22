%global __brp_check_rpaths %{nil}
%global packname  ggrasp
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian-Based Genome Representative Selector with Prioritization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-bgmm 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-bgmm 
Requires:         R-CRAN-colorspace 
Requires:         R-methods 

%description
Given a group of genomes and their relationship with each other, the
package clusters the genomes and selects the most representative members
of each cluster. Additional data can be provided to the prioritize certain
genomes. The results can be printed out as a list or a new phylogeny with
graphs of the trees and distance distributions also available. For
detailed introduction see: Thomas H Clarke, Lauren M Brinkac, Granger
Sutton, and Derrick E Fouts (2018), GGRaSP: a R-package for selecting
representative genomes using Gaussian mixture models, Bioinformatics,
bty300, <doi:10.1093/bioinformatics/bty300>.

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
