%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  superb
%global packver   0.95.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.95.15
Release:          1%{?dist}%{?buildtag}
Summary:          Summary Plots with Adjusted Error Bars

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-lsr >= 0.5
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-lsr >= 0.5
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Computes standard error and confidence interval of various descriptive
statistics under various designs and sampling schemes. The main function,
superbPlot(), return a plot. superbData() returns a dataframe with the
statistic and its precision interval so that other plotting package can be
used. See Cousineau and colleagues (2021) <doi:10.1177/25152459211035109>
or Cousineau (2017) <doi:10.5709/acp-0214-z> for a review as well as
Cousineau (2005) <doi:10.20982/tqmp.01.1.p042>, Morey (2008)
<doi:10.20982/tqmp.04.2.p061>, Baguley (2012)
<doi:10.3758/s13428-011-0123-7>, Cousineau & Laurencelle (2016)
<doi:10.1037/met0000055>, Cousineau & O'Brien (2014)
<doi:10.3758/s13428-013-0441-z>, Calderini & Harding
<doi:10.20982/tqmp.15.1.p001> for specific references.

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
