%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  heimdall
%global packver   1.0.737
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.737
Release:          1%{?dist}%{?buildtag}
Summary:          Drift Adaptable Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-daltoolbox 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-car 
Requires:         R-stats 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-daltoolbox 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-car 

%description
In streaming data analysis, it is crucial to detect significant shifts in
the data distribution or the accuracy of predictive models over time, a
phenomenon known as **concept drift**. The **heimdall** package aims to
identify when concept drift occurs and provide methodologies for adapting
models in non-stationary environments. It offers a range of
state-of-the-art techniques for detecting concept drift and maintaining
model performance. Additionally, **heimdall** provides tools for adapting
models in response to these changes, ensuring continuous and accurate
predictions in dynamic contexts. Methods for concept drift detection are
described in Tavares (2022) <doi:10.1007/s12530-021-09415-z>.

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
