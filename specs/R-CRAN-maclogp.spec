%global packname  maclogp
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Measures of Uncertainty for Model Selection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BMA 
BuildRequires:    R-CRAN-plot.matrix 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-utils 
Requires:         R-CRAN-BMA 
Requires:         R-CRAN-plot.matrix 
Requires:         R-CRAN-rlist 
Requires:         R-utils 

%description
Following the common types of measures of uncertainty for parameter
estimation, two measures of uncertainty were proposed for model selection,
see Liu, Li and Jiang (2020) <doi:10.1007/s11749-020-00737-9>. The first
measure is a kind of model confidence set that relates to the variation of
model selection, called Mac. The second measure focuses on error of model
selection, called LogP. They are all computed via bootstrapping. This
package provides functions to compute these two measures. Furthermore, a
similar model confidence set adapted from Bayesian Model Averaging can
also be computed using this package.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
