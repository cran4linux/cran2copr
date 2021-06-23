%global __brp_check_rpaths %{nil}
%global packname  bootSVD
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast, Exact Bootstrap Principal Component Analysis for High Dimensional Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ff 
Requires:         R-parallel 

%description
Implements fast, exact bootstrap Principal Component Analysis and Singular
Value Decompositions for high dimensional data, as described in
<doi:10.1080/01621459.2015.1062383> (see also <arXiv:1405.0922> ). For
data matrices that are too large to operate on in memory, users can input
objects with class 'ff' (see the 'ff' package), where the actual data is
stored on disk. In response, this package will implement a block matrix
algebra procedure for calculating the principal components (PCs) and
bootstrap PCs. Depending on options set by the user, the 'parallel'
package can be used to parallelize the calculation of the bootstrap PCs.

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
