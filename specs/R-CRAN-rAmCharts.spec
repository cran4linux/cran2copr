%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rAmCharts
%global packver   2.1.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.15
Release:          1%{?dist}%{?buildtag}
Summary:          JavaScript Charts Tool

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pipeR 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-methods 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-pipeR 
Requires:         R-CRAN-knitr 
Requires:         R-grDevices 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-zoo 

%description
Provides an R interface for using 'AmCharts' Library. Based on
'htmlwidgets', it provides a global architecture to generate 'JavaScript'
source code for charts. Most of classes in the library have their
equivalent in R with S4 classes; for those classes, not all properties
have been referenced but can easily be added in the constructors. Complex
properties (e.g. 'JavaScript' object) can be passed as named list. See
examples at <https://datastorm-open.github.io/introduction_ramcharts/> and
<https://www.amcharts.com/> for more information about the library. The
package includes the free version of 'AmCharts' Library. Its only
limitation is a small link to the web site displayed on your charts. If
you enjoy this library, do not hesitate to refer to this page
<https://www.amcharts.com/online-store/> to purchase a licence, and thus
support its creators and get a period of Priority Support. See also
<https://www.amcharts.com/about/> for more information about 'AmCharts'
company.

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
