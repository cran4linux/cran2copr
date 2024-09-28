%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dotwhisker
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          Dot-and-Whisker Plots of Regression Results

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-parameters 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggstance 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-grid 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-gridExtra 
Requires:         R-stats 
Requires:         R-CRAN-parameters 
Requires:         R-CRAN-performance 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggstance 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 

%description
Create quick and easy dot-and-whisker plots of regression results. It
takes as input either (1) a coefficient table in standard form or (2) one
(or a list of) fitted model objects (of any type that has methods
implemented in the 'parameters' package). It returns 'ggplot' objects that
can be further customized using tools from the 'ggplot2' package. The
package also includes helper functions for tasks such as rescaling
coefficients or relabeling predictor variables. See more methodological
discussion of the visualization and data management methods used in this
package in Kastellec and Leoni (2007) <doi:10.1017/S1537592707072209> and
Gelman (2008) <doi:10.1002/sim.3107>.

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
