%global packname  OUwie
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          2%{?dist}
Summary:          Analysis of Evolutionary Rates in an OU Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-paleotree 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-paleotree 
Requires:         R-CRAN-phangorn 
Requires:         R-stats 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-interp 
Requires:         R-grDevices 
Requires:         R-parallel 

%description
Estimates rates for continuous character evolution under Brownian motion
and a new set of Ornstein-Uhlenbeck based Hansen models that allow both
the strength of the pull and stochastic motion to vary across selective
regimes. Beaulieu et al (2012) <doi:10.1111/j.1558-5646.2012.01619.x>.

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
