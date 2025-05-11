%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BIDistances
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bioinformatic Distances

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-parallelDist 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-DataVisualizations 
BuildRequires:    R-CRAN-diptest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-parallelDist 
Requires:         R-parallel 
Requires:         R-CRAN-DataVisualizations 
Requires:         R-CRAN-diptest 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-vegan 
Requires:         R-methods 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-ggplot2 

%description
A selection of distances measures for bioinformatics data. Other important
distance measures for bioinformatics data are selected from the R package
'parallelDist'. A special distance measure for the Gene Ontology is
available.

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
