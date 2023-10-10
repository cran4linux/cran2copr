%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  parallelpam
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Partitioning-Around-Medoids (PAM) for Big Sets of Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-memuse >= 4.2.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-memuse >= 4.2.1
Requires:         R-CRAN-Rcpp >= 1.0.8

%description
Application of the Partitioning-Around-Medoids (PAM) clustering algorithm
described in Schubert, E. and Rousseeuw, P.J.: "Fast and eager k-medoids
clustering: O(k) runtime improvement of the PAM, CLARA, and CLARANS
algorithms." Information Systems, vol. 101, p. 101804, (2021).
<doi:10.1016/j.is.2021.101804>. It uses a binary format for storing and
retrieval of matrices developed for the 'jmatrix' package but the
functionality of 'jmatrix' is included here, so you do not need to install
it. Also, it is used by package 'scellpam', so if you have installed it,
you do not need to install this package. PAM can be applied to sets of
data whose dissimilarity matrix can be very big. It has been tested with
up to 100.000 points. It does this with the help of the code developed for
other package, 'jmatrix', which allows the matrix not to be loaded in 'R'
memory (which would force it to be of double type) but it gets from disk,
which allows using float (or even smaller data types). Moreover, the
dissimilarity matrix is calculated in parallel if the computer has several
cores so it can open many threads. The initial part of the PAM algorithm
can be done with the BUILD or LAB algorithms; the BUILD algorithm has been
implemented in parallel. The optimization phase implements the FastPAM1
algorithm, also in parallel. Finally, calculation of silhouette is
available and also implemented in parallel.

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
