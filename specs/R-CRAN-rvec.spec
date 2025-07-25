%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rvec
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Vectors Representing Random Variables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 

%description
Random vectors, called rvecs. An rvec holds multiple draws, but tries to
behave like a standard R vector, including working well in data frames.
Rvecs are useful for analysing output from a simulation or a Bayesian
analysis.

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
