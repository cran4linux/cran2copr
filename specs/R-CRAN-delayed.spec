%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  delayed
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Framework for Parallelizing Dependent Tasks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-rstackdeque 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-R.oo 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-future 
Requires:         R-CRAN-rstackdeque 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-R.oo 

%description
Mechanisms to parallelize dependent tasks in a manner that optimizes the
compute resources available. It provides access to "delayed" computations,
which may be parallelized using futures. It is, to an extent, a facsimile
of the 'Dask' library (<https://www.dask.org/>), for the 'Python'
language.

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
