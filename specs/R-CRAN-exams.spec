%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exams
%global packver   2.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Generation of Exams in R

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 

%description
Automatic generation of exams based on exercises in Markdown or LaTeX
format, possibly including R code for dynamic generation of exercise
elements. Exercise types include single-choice and multiple-choice
questions, arithmetic problems, string questions, and combinations thereof
(cloze). Output formats include standalone files (PDF, HTML, Docx, ODT,
...), Moodle XML, QTI 1.2, QTI 2.1, Blackboard, Canvas, OpenOlat, ILIAS,
TestVision, Particify, ARSnova, Kahoot!, Grasple, and TCExam. In addition
to fully customizable PDF exams, a standardized PDF format (NOPS) is
provided that can be printed, scanned, and automatically evaluated.

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
