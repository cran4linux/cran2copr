%global packname  secsse
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          2%{?dist}%{?buildtag}
Summary:          Several Examined and Concealed States-Dependent Speciation andExtinction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-DDD >= 4.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-apTreeshape 
BuildRequires:    R-CRAN-phylobase 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-DDD >= 4.0
Requires:         R-utils 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-apTreeshape 
Requires:         R-CRAN-phylobase 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-deSolve 

%description
Simultaneously infers state-dependent diversification across two or more
states of a single or multiple traits while accounting for the role of a
possible concealed trait. See Herrera-Alsina et al. 2019 Systematic
Biology 68: 317-328 <DOI:10.1093/sysbio/syy057>.

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
