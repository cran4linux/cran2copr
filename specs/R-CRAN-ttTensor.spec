%global packname  ttTensor
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tensor-Train Decomposition

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-tensorr 
BuildRequires:    R-CRAN-PTAk 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-tensorr 
Requires:         R-CRAN-PTAk 
Requires:         R-CRAN-Matrix 

%description
Tensor-train is a compact representation for higher-order tensors. Some
algorithms for performing tensor-train decomposition are available such as
TT-SVD, TT-WOPT, and TT-Cross. For the details of the algorithms, see I.
V. Oseledets (2011) <doi:10.1137/090752286>, Yuan Longao, et al (2017)
<arXiv:1709.02641>, I. V. Oseledets (2010)
<doi:10.1016/j.laa.2009.07.024>.

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
