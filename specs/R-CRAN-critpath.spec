%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  critpath
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Setting the Critical Path

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 

%description
Solving the problem of project management using CPM (Critical Path
Method), PERT (Program Evaluation and Review Technique) and LESS (Least
Cost Estimating and Scheduling) methods. The package sets the critical
path, schedule and Gantt chart. In addition, it allows to draw a graph
even with marked critical activities. For more information about project
management see: Taha H. A. "Operations Research. An Introduction" (2017,
ISBN:978-1-292-16554-7), Rama Murthy P. "Operations Research" (2007,
ISBN:978-81-224-2944-2), Yuval Cohen & Arik Sadeh (2006) "A New Approach
for Constructing and Generating AOA Networks", Journal of Engineering,
Computing and Architecture 1. 1-13, Konarzewska I., Jewczak M., Kucharski
A. (2020, ISBN:978-83-8220-112-3), Miszczyńska D., Miszczyński M. "Wybrane
metody badań operacyjnych" (2000, ISBN:83-907712-0-9).

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
