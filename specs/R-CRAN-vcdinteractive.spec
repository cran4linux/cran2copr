%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vcdinteractive
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Displays for Visualizing Categorical Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Interactive versions of the displays of the 'vcd' and 'vcdExtra' packages,
rendered as 'htmlwidgets'. Mosaic, association, sieve and doubledecker
plots share one widget, in which variables can be reordered, added or
removed and split directions changed on the fly, tiles report observed and
expected counts on hover, several kinds of residuals (Pearson, adjusted
standardized, deviance, Freeman-Tukey, Anscombe and residuals from a
robust fit) can be used for shading, and log-linear models can be
compared. Cells that depart significantly from the model are listed with
multiplicity-adjusted p-values. Further widgets provide pairwise mosaic
matrices with linked highlighting, fourfold displays with log odds ratio
plots, rootograms for discrete distributions, spinograms and conditional
density plots, correspondence analysis maps and association graphs. The
displays follow the strucplot framework of Meyer, Zeileis and Hornik
(2006) <doi:10.18637/jss.v017.i03> and Friendly and Meyer (2016, ISBN:
9781498725835).

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
