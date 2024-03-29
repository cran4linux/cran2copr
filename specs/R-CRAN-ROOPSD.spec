%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ROOPSD
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          R Object Oriented Programming for Statistical Distribution

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Lmoments 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Lmoments 
Requires:         R-CRAN-numDeriv 

%description
Statistical distribution in OOP (Object Oriented Programming) way. This
package proposes a R6 class interface to classic statistical distribution,
and new distributions can be easily added with the class AbstractDist. A
useful point is the generic fit() method for each class, which uses a
maximum likelihood estimation to find the parameters of a dataset, see,
e.g. Hastie, T. and al (2009) <isbn:978-0-387-84857-0>. Furthermore, the
rv_histogram class gives a non-parametric fit, with the same accessors
that for the classic distribution. Finally, three random generators useful
to build synthetic data are given: a multivariate normal generator, an
orthogonal matrix generator, and a symmetric positive definite matrix
generator, see Mezzadri, F. (2007) <arXiv:math-ph/0609050>.

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
