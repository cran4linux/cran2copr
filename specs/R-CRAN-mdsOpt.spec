%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mdsOpt
%global packver   0.7-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.7
Release:          1%{?dist}%{?buildtag}
Summary:          Searching for Optimal MDS Procedure for Metric and Interval-Valued Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-CRAN-clusterSim 
BuildRequires:    R-CRAN-symbolicDA 
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-spdep 
Requires:         R-CRAN-smacof 
Requires:         R-CRAN-clusterSim 
Requires:         R-CRAN-symbolicDA 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-spdep 

%description
Selecting the optimal multidimensional scaling (MDS) procedure for metric
data via metric MDS (ratio, interval, mspline) and nonmetric MDS
(ordinal). Selecting the optimal multidimensional scaling (MDS) procedure
for interval-valued data via metric MDS (ratio, interval,
mspline).Selecting the optimal multidimensional scaling procedure for
interval-valued data by varying all combinations of normalization and
optimization methods.Selecting the optimal MDS procedure for statistical
data referring to the evaluation of tourist attractiveness of Lower
Silesian counties. (Borg, I., Groenen, P.J.F., Mair, P. (2013)
<doi:10.1007/978-3-642-31848-1>, Walesiak, M. (2016)
<doi:10.15611/ekt.2016.2.01>, Walesiak, M. (2017)
<doi:10.15611/ekt.2017.3.01>).

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
