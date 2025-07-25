%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  latrend
%global packver   1.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Framework for Clustering Longitudinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 1.18
BuildRequires:    R-CRAN-data.table >= 1.15.4
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown >= 1.18
Requires:         R-CRAN-data.table >= 1.15.4
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-rlang 

%description
A framework for clustering longitudinal datasets in a standardized way.
The package provides an interface to existing R packages for clustering
longitudinal univariate trajectories, facilitating reproducible and
transparent analyses. Additionally, standard tools are provided to support
cluster analyses, including repeated estimation, model validation, and
model assessment. The interface enables users to compare results between
methods, and to implement and evaluate new methods with ease. The
'akmedoids' package is available from
<https://github.com/MAnalytics/akmedoids>.

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
