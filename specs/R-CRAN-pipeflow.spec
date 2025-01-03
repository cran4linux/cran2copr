%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pipeflow
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Lightweight, General-Purpose Data Analysis Pipelines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lgr 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-stats 
Requires:         R-utils 

%description
A lightweight yet powerful framework for building robust data analysis
pipelines. With 'pipeflow', you initialize a pipeline with your dataset
and construct workflows step by step by adding R functions. You can
modify, remove, or insert steps and parameters at any stage, while
'pipeflow' ensures the pipeline's integrity. Overall, this package offers
a beginner-friendly framework that simplifies and streamlines the
development of data analysis pipelines by making them modular, intuitive,
and adaptable.

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
