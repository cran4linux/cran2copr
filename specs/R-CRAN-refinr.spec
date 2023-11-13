%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  refinr
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster and Merge Similar Values Within a Character Vector

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-stringdist >= 0.9.5.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-stringdist >= 0.9.5.1
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-stringi 

%description
These functions take a character vector as input, identify and cluster
similar values, and then merge clusters together so their values become
identical. The functions are an implementation of the key collision and
ngram fingerprint algorithms from the open source tool Open Refine
<https://openrefine.org/>. More info on key collision and ngram
fingerprint can be found here
<https://openrefine.org/docs/technical-reference/clustering-in-depth>.

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
