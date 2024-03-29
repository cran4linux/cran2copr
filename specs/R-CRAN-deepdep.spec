%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deepdep
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Visualise and Explore the Deep Dependencies of R Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cranlogs 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-cranlogs 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 

%description
Provides tools for exploration of R package dependencies. The main
deepdep() function allows to acquire deep dependencies of any package and
plot them in an elegant way. It also adds some popularity measures for the
packages e.g. in the form of download count through the 'cranlogs'
package. Uses the CRAN metadata database <http://crandb.r-pkg.org> and
Bioconductor metadata <https://bioconductor.org>. Other data acquire
functions are: get_dependencies(), get_downloads() and get_description().
The deepdep_shiny() function runs shiny application that helps to produce
a nice 'deepdep' plot.

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
