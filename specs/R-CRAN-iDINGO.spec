%global __brp_check_rpaths %{nil}
%global packname  iDINGO
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Integrative Differential Network Analysis in Genomics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-GGMridge 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-glasso 
Requires:         R-parallel 
Requires:         R-CRAN-GGMridge 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-scales 

%description
Fits covariate dependent partial correlation matrices for integrative
models to identify differential networks between two groups. The methods
are described in Class et. al., (2018) <doi:10.1093/bioinformatics/btx750>
and Ha et. al., (2015) <doi:10.1093/bioinformatics/btv406>.

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
