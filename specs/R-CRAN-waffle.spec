%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  waffle
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Create Waffle Chart Visualizations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 

%description
Square pie charts (a.k.a. waffle charts) can be used to communicate parts
of a whole for categorical quantities. To emulate the percentage view of a
pie chart, a 10x10 grid should be used with each square representing 1%% of
the total. Modern uses of waffle charts do not necessarily adhere to this
rule and can be created with a grid of any rectangular shape. Best
practices suggest keeping the number of categories small, just as should
be done when creating pie charts. Tools are provided to create waffle
charts as well as stitch them together, and to use glyphs for making
isotype pictograms.

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
