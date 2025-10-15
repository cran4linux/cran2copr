%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NCA
%global packver   4.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Necessary Condition Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-truncnorm 

%description
Performs a Necessary Condition Analysis (NCA). (Dul, J. 2016. Necessary
Condition Analysis (NCA). ''Logic and Methodology of 'Necessary but not
Sufficient' causality." Organizational Research Methods 19(1), 10-52)
<doi:10.1177/1094428115584005>. NCA identifies necessary (but not
sufficient) conditions in datasets, where x causes (e.g. precedes) y.
Instead of drawing a regression line ''through the middle of the data'' in
an xy-plot, NCA draws the ceiling line. The ceiling line y = f(x)
separates the area with observations from the area without observations.
(Nearly) all observations are below the ceiling line: y <= f(x). The empty
zone is in the upper left hand corner of the xy-plot (with the convention
that the x-axis is ''horizontal'' and the y-axis is ''vertical'' and that
values increase ''upwards'' and ''to the right''). The ceiling line is a
(piecewise) linear non-decreasing line: a linear step function or a
straight line. It indicates which level of x (e.g. an effort or input) is
necessary but not sufficient for a (desired) level of y (e.g. good
performance or output). A quick start guide for using this package can be
found here: <https://repub.eur.nl/pub/78323/> or
<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2624981>.

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
