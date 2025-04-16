%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ConsRank
%global packver   2.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Compute the Median Ranking(s) According to the Kemeny's Axiomatic Approach

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlist >= 0.4.2
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-rlist >= 0.4.2
Requires:         R-CRAN-rgl 
Requires:         R-methods 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-tidyr 

%description
Compute the median ranking according to the Kemeny's axiomatic approach.
Rankings can or cannot contain ties, rankings can be both complete or
incomplete. The package contains both branch-and-bound algorithms and
heuristic solutions recently proposed. The searching space of the solution
can either be restricted to the universe of the permutations or
unrestricted to all possible ties. The package also provide some useful
utilities for deal with preference rankings, including both element-weight
Kemeny distance and correlation coefficient. This release declare as
deprecated some functions that are still in the package for compatibility.
Next release will not contains these functions. Please type
'?ConsRank-deprecated' Essential references: Emond, E.J., and Mason, D.W.
(2002) <doi:10.1002/mcda.313>; D'Ambrosio, A., Amodio, S., and Iorio, C.
(2015) <doi:10.1285/i20705948v8n2p198>; Amodio, S., D'Ambrosio, A., and
Siciliano R. (2016) <doi:10.1016/j.ejor.2015.08.048>; D'Ambrosio, A.,
Mazzeo, G., Iorio, C., and Siciliano, R. (2017)
<doi:10.1016/j.cor.2017.01.017>; Albano, A., and Plaia, A. (2021)
<doi:10.1285/i20705948v14n1p117>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
