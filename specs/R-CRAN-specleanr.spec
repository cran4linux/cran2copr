%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  specleanr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Detecting Environmental Outliers in Data Analysis Pipelines

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-isotree 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-robust 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-usdm 
BuildRequires:    R-CRAN-mgcv 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-isotree 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-robust 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-usdm 
Requires:         R-CRAN-mgcv 

%description
A framework used to detect and handle outliers during data analysis
workflows. Outlier detection is a statistical concept with applications in
data analysis workflows, highlighting records that are suspiciously high
or low. Outlier detection in distribution models was initiated by Chapman
(1991) (available at
<https://www.researchgate.net/publication/332537800_Quality_control_and_validation_of_point-sourced_environmental_resource_data>),
who developed the reverse jackknifing method. The concept was further
developed and incorporated into different R packages, including 'flexsdm'
(Velazco et al., 2022, <doi:10.1111/2041-210X.13874>) and 'biogeo'
(Robertson et al., 2016 <doi:10.1111/ecog.02118>). We compiled various
outlier detection methods obtained from the literature, including those
elaborated in Dastjerdy et al. (2023) <doi:10.3390/geotechnics3020022> and
Liu et al. (2008) <doi:10.1109/ICDM.2008.17>. In this package, we
introduced the ensembling aspect, where multiple outlier detection methods
are used to flag the record as either an absolute outlier. The concept can
also be applied in general data analysis, as well as during the
development of species distribution models.

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
