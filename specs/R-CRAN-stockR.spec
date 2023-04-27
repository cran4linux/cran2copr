%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stockR
%global packver   1.0.76
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.76
Release:          1%{?dist}%{?buildtag}
Summary:          Identifying Stocks in Genetic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-gtools 
Requires:         R-parallel 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-methods 

%description
Provides a mixture model for clustering individuals (or sampling groups)
into stocks based on their genetic profile. Here, sampling groups are
individuals that are sure to come from the same stock (e.g. breeding
adults or larvae). The mixture (log-)likelihood is maximised using the
EM-algorithm after finding good starting values via a K-means clustering
of the genetic data. Details can be found in: Foster, S. D.; Feutry, P.;
Grewe, P. M.; Berry, O.; Hui, F. K. C. & Davies (2020)
<doi:10.1111/1755-0998.12920>.

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
