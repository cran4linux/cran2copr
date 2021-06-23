%global __brp_check_rpaths %{nil}
%global packname  o2geosocial
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Reconstruction of Transmission Chains from Surveillance Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-outbreaker2 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-outbreaker2 

%description
Bayesian reconstruction of who infected whom during past outbreaks using
routinely-collected surveillance data. Inference of transmission trees
using genotype, age specific social contacts, distance between cases and
onset dates of the reported cases. (Robert A, Kucharski AJ, Gastanaduy PA,
Paul P, Funk S. 2020 <doi:10.1098/rsif.2020.0084>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
