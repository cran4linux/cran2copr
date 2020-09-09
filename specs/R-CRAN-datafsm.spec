%global packname  datafsm
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Finite State Machine Models from Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-Rcpp 

%description
Automatic generation of finite state machine models of dynamic
decision-making that both have strong predictive power and are
interpretable in human terms. We use an efficient model representation and
a genetic algorithm-based estimation process to generate simple
deterministic approximations that explain most of the structure of complex
stochastic processes. We have applied the software to empirical data, and
demonstrated it's ability to recover known data-generating processes by
simulating data with agent-based models and correctly deriving the
underlying decision models for multiple agent models and degrees of
stochasticity.

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
