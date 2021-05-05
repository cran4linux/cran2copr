%global packname  LSMRealOptions
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Value American and Real Options Through LSM Simulation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-stats 
Requires:         R-CRAN-lifecycle 

%description
The least-squares Monte Carlo (LSM) simulation method is a popular method
for the approximation of the value of early and multiple exercise options.
'LSMRealOptions' provides implementations of the LSM simulation method to
value American option products and capital investment projects through
real options analysis. 'LSMRealOptions' values capital investment projects
with cash flows dependent upon underlying state variables that are
stochastically evolving, providing analysis into the timing and critical
values at which investment is optimal. 'LSMRealOptions' provides
flexibility in the stochastic processes followed by underlying assets, the
number of state variables, basis functions and underlying asset
characteristics to allow a broad range of assets to be valued through the
LSM simulation method. Real options projects are further able to be valued
whilst considering construction periods, time-varying initial capital
expenditures and path-dependent operational flexibility including the
ability to temporarily shutdown or permanently abandon projects after
initial investment has occurred. The LSM simulation method was first
presented in the prolific work of Longstaff and Schwartz (2001)
<doi:10.1093/rfs/14.1.113>.

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
