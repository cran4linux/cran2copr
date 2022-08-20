%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  luz
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Higher Level 'API' for 'torch'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-torch >= 0.5.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-zeallot 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-torch >= 0.5.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-zeallot 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-coro 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-cli 

%description
A high level interface for 'torch' providing utilities to reduce the the
amount of code needed for common tasks, abstract away torch details and
make the same code work on both the 'CPU' and 'GPU'. It's flexible enough
to support expressing a large range of models. It's heavily inspired by
'fastai' by Howard et al. (2020) <arXiv:2002.04688>, 'Keras' by Chollet et
al. (2015) and 'PyTorch Lightning' by Falcon et al. (2019)
<doi:10.5281/zenodo.3828935>.

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
