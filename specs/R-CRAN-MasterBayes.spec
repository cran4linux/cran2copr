%global packname  MasterBayes
%global packver   2.57
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.57
Release:          2%{?dist}%{?buildtag}
Summary:          ML and MCMC Methods for Pedigree Reconstruction and Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-genetics 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-genetics 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-kinship2 
Requires:         R-methods 
Requires:         R-stats 

%description
The primary aim of 'MasterBayes' is to use MCMC techniques to integrate
over uncertainty in pedigree configurations estimated from molecular
markers and phenotypic data.  Emphasis is put on the marginal distribution
of parameters that relate the phenotypic data to the pedigree. All
simulation is done in compiled 'C++' for efficiency.

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

%files
%{rlibdir}/%{packname}
