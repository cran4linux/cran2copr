%global __brp_check_rpaths %{nil}
%global packname  ouxy
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          2%{?dist}%{?buildtag}
Summary:          Model of Adaptive Trait Evolution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Sim.DiffProc 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-abc 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-TreeSim 
BuildRequires:    R-CRAN-adephylo 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-EasyABC 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Sim.DiffProc 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-abc 
Requires:         R-CRAN-phytools 
Requires:         R-nlme 
Requires:         R-CRAN-TreeSim 
Requires:         R-CRAN-adephylo 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-EasyABC 
Requires:         R-utils 

%description
Performs statistical inference on the models of adaptive trait evolution
under approximate Bayesian computation. This can simulate traits from four
models, compute trait data summary statistics. Parameters are estimated
under Approximate Bayesian Computation, model selection as well as
posterior parameter mean will be reported. Users need to enter a
comparative dataset and a phylogenetic tree.

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
