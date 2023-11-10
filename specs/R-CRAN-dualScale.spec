%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dualScale
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dual Scaling Analysis of Data

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-eba 
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-utils 
Requires:         R-CRAN-eba 
Requires:         R-CRAN-ff 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-grid 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixcalc 
Requires:         R-stats 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-glue 
Requires:         R-utils 

%description
Dual Scaling, developed by Professor Shizuhiko Nishisato (1994, ISBN:
0-9691785-3-6), is a fundamental technique in multivariate analysis used
for data scaling and correspondence analysis. Its utility lies in its
ability to represent multidimensional data in a lower-dimensional space,
making it easier to visualize and understand underlying patterns in
complex data. This technique has been implemented to handle various types
of data, including Contingency and Frequency data (CF), Multiple-Choice
data (MC), Sorting data (SO), Paired-Comparison data (PC), and Rank-Order
data (RO), providing users with a powerful tool to explore relationships
between variables and observations in various fields, from sociology to
ecology, enabling deeper and more efficient analysis of multivariate
datasets.

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
