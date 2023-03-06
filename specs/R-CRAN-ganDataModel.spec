%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ganDataModel
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Build a Metric Subspaces Data Model for a Data Source

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-tensorflow >= 2.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-tensorflow >= 2.0.0
Requires:         R-CRAN-Rcpp >= 1.0.3

%description
Neural networks are applied to create a density value function which
approximates density values for a data source. The trained neural network
is analyzed for different levels. For each level metric subspaces with
density values above a level are determined. The obtained set of metric
subspaces and the trained neural network are assembled into a data model.
A prerequisite is the definition of a data source, the generation of
generative data and the calculation of density values. These tasks are
executed using package 'ganGenerativeData'
<https://cran.r-project.org/package=ganGenerativeData>.

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
