%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gsMeanFreq
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Group Sequential Clinical Trial Designs for Composite Endpoints

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-gsDesign 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bdsmatrix 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-gsDesign 
Requires:         R-stats 
Requires:         R-CRAN-bdsmatrix 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-survival 

%description
Simulating composite endpoints with recurrent and terminal events under
staggered entry, and for constructing one- and two-sample group sequential
test statistics and monitoring boundaries based on the mean frequency
function. Details will be available in an upcoming publication.

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
