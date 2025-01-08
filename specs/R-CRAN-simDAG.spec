%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simDAG
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Data from a DAG and Associated Node Information

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-igraph 

%description
Simulate complex data from a given directed acyclic graph and information
about each individual node. Root nodes are simply sampled from the
specified distribution. Child Nodes are simulated according to one of many
implemented regressions, such as logistic regression, linear regression,
poisson regression and more. Also includes a comprehensive framework for
discrete-time simulation, which can generate even more complex
longitudinal data.

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
