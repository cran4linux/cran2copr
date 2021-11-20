%global __brp_check_rpaths %{nil}
%global packname  FairMclus
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering for Data with Sensitive Attribute

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-tidyr 
Requires:         R-parallel 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-cluster 
Requires:         R-base 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Clustering for categorical and mixed-type of data, to preventing
classification biases due to race, gender or others sensitive attributes.
This algorithm is an extension of the methodology proposed by "Santos &
Heras (2020) <doi:10.28945/4643>".

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
