%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RKEEL
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Using 'KEEL' in R Code

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RKEELdata >= 1.0.5
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-pmml 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-downloader 
Requires:         R-CRAN-RKEELdata >= 1.0.5
Requires:         R-CRAN-R6 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-pmml 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-downloader 

%description
'KEEL' is a popular 'Java' software for a large number of different
knowledge data discovery tasks. This package takes the advantages of
'KEEL' and R, allowing to use 'KEEL' algorithms in simple R code. The
implemented R code layer between R and 'KEEL' makes easy both using 'KEEL'
algorithms in R as implementing new algorithms for 'RKEEL' in a very
simple way. It includes more than 100 algorithms for classification,
regression, preprocess, association rules and imbalance learning, which
allows a more complete experimentation process. For more information about
'KEEL', see <http://www.keel.es/>.

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
