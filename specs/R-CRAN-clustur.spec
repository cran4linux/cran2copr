%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clustur
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-utils 

%description
A tool that implements the clustering algorithms from 'mothur' (Schloss PD
et al. (2009) <doi:10.1128/AEM.01541-09>). 'clustur' make use of the
cluster() and make.shared() command from 'mothur'. Our cluster() function
has five different algorithms implemented: 'OptiClust', 'furthest',
'nearest', 'average', and 'weighted'. 'OptiClust' is an optimized
clustering method for Operational Taxonomic Units, and you can learn more
here, (Westcott SL, Schloss PD (2017)
<doi:10.1128/mspheredirect.00073-17>). The make.shared() command is always
applied at the end of the clustering command. This functionality allows us
to generate and create clustering and abundance data efficiently.

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
