%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rpymat
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Easy to Configure an Isolated 'Python' Environment

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.7.3
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-IRkernel >= 1.3
BuildRequires:    R-CRAN-reticulate >= 1.21
BuildRequires:    R-CRAN-fastmap >= 1.1.0
BuildRequires:    R-CRAN-rappdirs >= 0.3.3
BuildRequires:    R-CRAN-rstudioapi >= 0.13
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite >= 1.7.3
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-IRkernel >= 1.3
Requires:         R-CRAN-reticulate >= 1.21
Requires:         R-CRAN-fastmap >= 1.1.0
Requires:         R-CRAN-rappdirs >= 0.3.3
Requires:         R-CRAN-rstudioapi >= 0.13
Requires:         R-utils 

%description
Aims to create a single isolated 'Miniconda' and 'Python' environment for
reproducible pipeline scripts. The package provides utilities to run
system command within the 'conda' environment, making it easy to install,
launch, manage, and stop 'Jupyter-lab'.

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
