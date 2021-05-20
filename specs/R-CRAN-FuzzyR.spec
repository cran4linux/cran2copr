%global packname  FuzzyR
%global packver   2.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fuzzy Logic Toolkit for R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-splines 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-plyr 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-graphics 

%description
Design and simulate fuzzy logic systems using Type-1 and Interval Type-2
Fuzzy Logic. This toolkit includes with graphical user interface (GUI) and
an adaptive neuro- fuzzy inference system (ANFIS). This toolkit is a
continuation from the previous package ('FuzzyToolkitUoN'). Produced by
the Intelligent Modelling & Analysis Group (IMA) and Lab for UnCertainty
In Data and decision making (LUCID), University of Nottingham. A big thank
you to the many people who have contributed to the development/evaluation
of the toolbox. Please cite the toolbox and the corresponding paper
<doi:10.1109/FUZZ48607.2020.9177780> when using it. More related papers
can be found in the NEWS.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
