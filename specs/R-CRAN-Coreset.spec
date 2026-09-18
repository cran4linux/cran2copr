%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Coreset
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Diversity, Dispersion, and Coverage Subset Selection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Solves discrete location objectives on a distance matrix or Euclidean
coordinate set. The Max-Min Diversity (MMDP / p-dispersion) objective,
which maximizes the minimum pairwise distance within a selection of k
items, is solved by farthest-first selection (Gonzalez 1985)
<doi:10.1016/0304-3975(85)90224-5>; the DropAdd tabu-search heuristic
(Porumbel, Hao & Glover 2011) <doi:10.1007/s10479-011-0898-z>, GRASP with
path-relinking (Resende, Marti, Gallego & Duarte 2010)
<doi:10.1016/j.cor.2008.05.011>, and an exact node-packing integer program
(Sayyady & Fathi 2016) <doi:10.1016/j.ejor.2016.02.026>. The Max-Mean
Dispersion objective, which selects a subset of unrestricted size
maximising the sum of its pairwise distances divided by the number of
selected elements, is solved by reinforcement-learning-guided tabu search
(Nijimbere et al. 2020) <doi:10.3934/jimo.2020115>. The discrete k-centre
(min-max covering / facility location) objective, which chooses k centres
to minimise the largest distance from any point to its nearest centre, is
solved via the CDSh heuristic (Garcia-Diaz et al. 2017
<doi:10.1007/s10732-017-9345-x>, 2019 <doi:10.1109/ACCESS.2019.2933875>),
and an exact minimum-cover integer program. The maximum-entropy (maxdet)
objective, which maximises the log-determinant of a similarity kernel
built from the distances (Shewry & Wynn 1987
<doi:10.1080/02664768700000020>; the mode of a determinantal point
process, Kulesza & Taskar 2012 <doi:10.1561/2200000044>), is solved by
greedy pivoted-Cholesky selection and, for small instances, exact
enumeration.

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
