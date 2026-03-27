%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rtemis
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning and Visualization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-cli 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-future 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-cli 

%description
Machine learning and visualization package with an 'S7' backend featuring
comprehensive type checking and validation, paired with an efficient
functional user-facing API. train(), cluster(), and decomp() provide
one-call access to supervised and unsupervised learning. All configuration
steps are performed using setup functions and validated. A single call to
train() handles preprocessing, hyperparameter tuning, and testing with
nested resampling. Supports 'data.frame', 'data.table', and 'tibble'
inputs, parallel execution, and interactive visualizations. The package
first appeared in E.D. Gennatas (2017)
<https://repository.upenn.edu/entities/publication/d81892ea-3087-4b71-a6f5-739c58626d64>.

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
