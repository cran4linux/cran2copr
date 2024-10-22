%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statforbiology
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Data Analyses in Biology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-drc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-drcte 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-multcompView 
Requires:         R-CRAN-drc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-car 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-emmeans 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-drcte 
Requires:         R-CRAN-multcomp 
Requires:         R-utils 
Requires:         R-CRAN-multcompView 

%description
Contains several tools for nonlinear regression analyses and general data
analysis in biology and agriculture. Contains also datasets for practicing
and teaching purposes. Supports the blog: Onofri (2024) "Fixing the bridge
between biologists and statisticians" <https://www.statforbiology.com> and
the book: Onofri (2024) "Experimental Methods in Agriculture"
<https://www.statforbiology.com/_statbookeng/>. The blog is a collection
of short articles aimed at improving the efficiency of communication
between biologists and statisticians, as pointed out in Kozak (2016)
<doi:10.1590/0103-9016-2015-0399>, spreading a better awareness of the
potential usefulness, beauty and limitations of biostatistic.

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
