%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  counterfactuals
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Counterfactual Explanations

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-StatMatch 
BuildRequires:    R-CRAN-iml 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-miesmuschel 
BuildRequires:    R-CRAN-bbotk 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-StatMatch 
Requires:         R-CRAN-iml 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-miesmuschel 
Requires:         R-CRAN-bbotk 

%description
Modular and unified R6-based interface for counterfactual explanation
methods. The following methods are currently implemented: Burghmans et al.
(2022) <arXiv:2104.07411>, Dandl et al. (2020)
<doi:10.1007/978-3-030-58112-1_31> and Wexler et al. (2019)
<doi:10.1109/TVCG.2019.2934619>. Optional extensions allow these methods
to be applied to a variety of models and use cases. Once generated, the
counterfactuals can be analyzed and visualized by provided
functionalities.

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
