%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ConsRank
%global packver   3.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Compute the Median Ranking(s) According to the Kemeny's Axiomatic Approach

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-rlist >= 0.4.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-rlist >= 0.4.2
Requires:         R-methods 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-Rcpp 

%description
Compute the median ranking according to the Kemeny's axiomatic approach.
Rankings can or cannot contain ties, rankings can be both complete or
incomplete. The package contains both branch-and-bound algorithms and
heuristic solutions. The search space of the solution can be the universe
of all rankings with ties, the permutations, or the bucket orders with a
given number of buckets or with a given pattern of bucket sizes, top-k
lists included. The package also provides some useful utilities to deal
with preference rankings, including the element-weight Kemeny distance and
correlation coefficient. Essential references: Emond, E.J., and Mason,
D.W. (2002) <doi:10.1002/mcda.313>; D'Ambrosio, A., Amodio, S., and Iorio,
C. (2015) <doi:10.1285/i20705948v8n2p198>; Amodio, S., D'Ambrosio, A., and
Siciliano R. (2016) <doi:10.1016/j.ejor.2015.08.048>; D'Ambrosio, A.,
Mazzeo, G., Iorio, C., and Siciliano, R. (2017)
<doi:10.1016/j.cor.2017.01.017>; Albano, A., and Plaia, A. (2021)
<doi:10.1285/i20705948v14n1p117>; D'Ambrosio, A., Iorio, C., Staiano, M.
and Siciliano, R (2019) <doi:10.1007/s00180-018-0858-z>; Romano, M.,
Coraggio, L., Conversano, C., and D'Ambrosio, A. (2026)
<doi:10.48550/arXiv.2611.28925>.

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
