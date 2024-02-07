%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OlympicRshiny
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          'Shiny' Application for Olympic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.4
BuildRequires:    R-CRAN-golem >= 0.3.5
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-summarytools 
Requires:         R-CRAN-shiny >= 1.7.4
Requires:         R-CRAN-golem >= 0.3.5
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-summarytools 

%description
'Shiny' Application to visualize Olympic Data. From 1896 to 2016. Even
Winter Olympics events are included. Data is from Kaggle at
<https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results>.

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
