%global packname  scTenifoldNet
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Construct and Compare scGRN from Single-Cell Transcriptomic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-RSpectra 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-MASS 

%description
A workflow based on machine learning methods to construct and compare
single-cell gene regulatory networks (scGRN) using single-cell RNA-seq
(scRNA-seq) data collected from different conditions. Uses principal
component regression, tensor decomposition, and manifold alignment, to
accurately identify even subtly shifted gene expression programs.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
