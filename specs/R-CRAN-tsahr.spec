%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsahr
%global packver   0.2.8.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8.17
Release:          1%{?dist}%{?buildtag}
Summary:          Trial Sequential Analysis for Meta-Analyses of Hazard Ratios

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-readxl 
Requires:         R-stats 
Requires:         R-utils 

%description
Performs Trial Sequential Analysis (TSA) for meta-analyses of
time-to-event outcomes reported as hazard ratios. Implements the
Schoenfeld required-events sample-size formula generalised for unequal
allocation, the Diversity (D-squared) heterogeneity adjustment of
Wetterslev et al. (2009), and O'Brien-Fleming-type alpha- and
beta-spending trial sequential monitoring boundaries computed at the
inverse-variance information based on observed study-level log-HR standard
errors (not merely event counts), via a compiled (C++) recursive numerical
integration engine ported from the R package 'RTSA' (Soerensen, Olsen,
Lange and Gluud; an R implementation of the Trial Sequential Analysis
software of the Copenhagen Trial Unit, <https://ctu.dk/tools>), with no
fixed software-imposed limit on the number of looks (subject to available
computational resources). Produces a cumulative Z-curve plot with
efficacy, futility, and conventional significance boundaries. Methodology
follows Miladinovic et al. (2013) <doi:10.1016/j.jclinepi.2012.11.007> and
Wetterslev et al. (2009) <doi:10.1186/1471-2288-9-86>.

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
