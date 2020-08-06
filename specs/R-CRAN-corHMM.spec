%global packname  corHMM
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          1%{?dist}
Summary:          Hidden Markov Models of Character Evolution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-MASS 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-phytools 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-corpcor 
Requires:         R-MASS 
Requires:         R-nnet 
Requires:         R-CRAN-phangorn 
Requires:         R-parallel 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-phytools 

%description
Fits hidden Markov models of discrete character evolution which allow
different transition rate classes on different portions of a phylogeny.
Beaulieu et al (2013) <doi:10.1093/sysbio/syt034>.

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
