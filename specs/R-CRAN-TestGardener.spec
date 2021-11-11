%global __brp_check_rpaths %{nil}
%global packname  TestGardener
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Analysis of Test and Rating Scale Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-utf8 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-utf8 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 

%description
Develop, evaluate, and score multiple choice examinations, psychological
scales, questionnaires, and similar types of data involving sequences of
choices among one or more sets of answers. Using the package does not
require any formal statistical knowledge beyond what would be provided by
a first course in statistics in a social science department.  There the
user would encounter the concept of probability and how it is used to
model data and make decisions, and would become familiar with basic
mathematical and statistical notation. The essential aspects of each
display were designed to be self-explanatory, although more statistically
sophisticated users will also find information that they may find helpful.
Most of the output is in graphical form. Two recent papers on the
methodology are Ramsay, James; Li, Juan; Wiberg, Marie (2020)
<doi:10.3390/psych2040026> and Ramsay, James; Wiberg, Marie; Li, Juan
(2019) <doi:10.3102/1076998619885636>.

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
