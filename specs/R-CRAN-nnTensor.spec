%global __brp_check_rpaths %{nil}
%global packname  nnTensor
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Negative Tensor Decomposition

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-tagcloud 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-tagcloud 
Requires:         R-CRAN-ggplot2 

%description
Some functions for performing non-negative matrix factorization,
non-negative CANDECOMP/PARAFAC (CP) decomposition, non-negative Tucker
decomposition, and generating toy model data. See Andrzej Cichock et al
(2009) <doi:10.1002/9780470747278> and the reference section of GitHub
README.md <https://github.com/rikenbit/nnTensor>, for details of the
methods.

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
