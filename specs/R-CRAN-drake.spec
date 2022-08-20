%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drake
%global packver   7.13.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.13.4
Release:          1%{?dist}%{?buildtag}
Summary:          A Pipeline Toolkit for Reproducible Computation at Scale

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-storr >= 1.1.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-digest >= 0.6.21
BuildRequires:    R-CRAN-txtq >= 0.2.3
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-vctrs >= 0.2.0
BuildRequires:    R-CRAN-base64url 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
Requires:         R-CRAN-storr >= 1.1.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-digest >= 0.6.21
Requires:         R-CRAN-txtq >= 0.2.3
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-vctrs >= 0.2.0
Requires:         R-CRAN-base64url 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-utils 

%description
A general-purpose computational engine for data analysis, drake rebuilds
intermediate data objects when their dependencies change, and it skips
work when the results are already up to date.  Not every execution starts
from scratch, there is native support for parallel and distributed
computing, and completed projects have tangible evidence that they are
reproducible.  Extensive documentation, from beginner-friendly tutorials
to practical examples and more, is available at the reference website
<https://docs.ropensci.org/drake/> and the online manual
<https://books.ropensci.org/drake/>.

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
