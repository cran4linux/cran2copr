%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  funModeling
%global packver   1.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.5
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Data Analysis and Data Preparation Tool-Box

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 3.17.1
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-Hmisc >= 3.17.1
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lazyeval 
Requires:         R-utils 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-stringr 

%description
Around 10%% of almost any predictive modeling project is spent in
predictive modeling, 'funModeling' and the book Data Science Live Book
(<https://livebook.datascienceheroes.com/>) are intended to cover
remaining 90%%: data preparation, profiling, selecting best variables
'dataViz', assessing model performance and other functions.

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
