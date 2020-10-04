%global packname  EpiModel
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Mathematical Modeling of Infectious Disease Dynamics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-tergm >= 3.5
BuildRequires:    R-CRAN-ergm >= 3.10
BuildRequires:    R-CRAN-tergmLite >= 2.2.0
BuildRequires:    R-CRAN-deSolve >= 1.21
BuildRequires:    R-CRAN-network >= 1.13
BuildRequires:    R-CRAN-networkDynamic >= 0.9
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-tergm >= 3.5
Requires:         R-CRAN-ergm >= 3.10
Requires:         R-CRAN-tergmLite >= 2.2.0
Requires:         R-CRAN-deSolve >= 1.21
Requires:         R-CRAN-network >= 1.13
Requires:         R-CRAN-networkDynamic >= 0.9
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-ggplot2 

%description
Tools for simulating mathematical models of infectious disease dynamics.
Epidemic model classes include deterministic compartmental models,
stochastic individual-contact models, and stochastic network models.
Network models use the robust statistical methods of exponential-family
random graph models (ERGMs) from the Statnet suite of software packages in
R. Standard templates for epidemic modeling include SI, SIR, and SIS
disease types. EpiModel features an API for extending these templates to
address novel scientific research aims.

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
