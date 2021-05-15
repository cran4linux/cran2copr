%global packname  pomdp
%global packver   0.99.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.2
Release:          1%{?dist}%{?buildtag}
Summary:          Solver for Partially Observable Markov Decision Processes (POMDP)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Ternary 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Ternary 
Requires:         R-CRAN-visNetwork 

%description
Provides the infrastructure to define and analyze the solutions of
Partially Observable Markov Decision Processes (POMDP) models. The package
includes pomdp-solve to solve POMDPs using a variety of exact and
approximate value iteration algorithms. Smallwood and Sondik (1973)
<doi:10.1287/opre.21.5.1071>.

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
