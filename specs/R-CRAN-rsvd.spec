%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rsvd
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Randomized Singular Value Decomposition

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.7.0
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix >= 1.7.0
Requires:         R-methods 

%description
Computes low-rank matrix approximations for dimension reduction, data
analysis, and compression. Randomized algorithms use random weighted
combinations of the input to find a small subspace, then factorize the
projected matrix. This can reduce the work when the requested rank is
small relative to the matrix dimensions and the input has a useful
low-rank approximation. Methods include singular value decomposition,
principal component analysis, QB factorization, and interpolative and CUR
decompositions. Robust principal component analysis separates a matrix
into low-rank and entrywise sparse components. Selected routines support
sparse matrices, including principal component analysis with implicit
centering and scaling. Plotting functions display scores, loadings, and
explained variance. See Erichson et al. (2019) <doi:10.18637/jss.v089.i11>
for the algorithms and examples of their use.

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
