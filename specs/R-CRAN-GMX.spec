%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GMX
%global packver   0.9-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Extended Graphical Model Checks for the Rasch Family of Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-psychotools 
Requires:         R-CRAN-psychotools 

%description
The function plotLRT() draws pairwise graphical model checks for the Rasch
Model (RM; Rasch, 1960), the Partial Credit Model(PCM; Masters, 1982), and
the Rating Scale Model (RSM; Andrich, 1978) using the output object of
eRm::LRtest(). The function cLRT() provides a conditional Likelihood Ratio
Test (Andersen, 1973), using the routines of 'psychotools'. Users may
choose to plot the threshold parameters, the cumulative thresholds, the
average thresholds per item, or the person parameters. Extended coloring
options allow for automated item-wise or threshold-wise coloring. For
multi-group splits, all pairwise group comparisons are drawn
automatically. For more details see Andersen (1973)
<doi:10.1007/BF02291180>, Andrich (1978) <doi:10.1007/BF02293814>, Masters
(1982) <doi:10.1007/BF02296272> and Rasch (1960, ISBN:9780598554512).

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
