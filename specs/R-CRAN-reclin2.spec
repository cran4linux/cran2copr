%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reclin2
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Record Linkage Toolkit

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringdist 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 

%description
Functions to assist in performing probabilistic record linkage and
deduplication: generating pairs, comparing records, em-algorithm for
estimating m- and u-probabilities (I. Fellegi & A. Sunter (1969)
<doi:10.1080/01621459.1969.10501049>, T.N. Herzog, F.J. Scheuren, & W.E.
Winkler (2007), "Data Quality and Record Linkage Techniques",
ISBN:978-0-387-69502-0), forcing one-to-one matching. Can also be used for
pre- and post-processing for machine learning methods for record linkage.
Focus is on memory, CPU performance and flexibility.

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
