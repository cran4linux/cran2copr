%global __brp_check_rpaths %{nil}
%global packname  bgmm
%global packver   1.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.5
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Mixture Modeling Algorithms and the Belief-Based Mixture Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-combinat 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-car 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-combinat 

%description
Two partially supervised mixture modeling methods: soft-label and
belief-based modeling are implemented. For completeness, we equipped the
package also with the functionality of unsupervised, semi- and fully
supervised mixture modeling.  The package can be applied also to selection
of the best-fitting from a set of models with different component numbers
or constraints on their structures. For detailed introduction see:
Przemyslaw Biecek, Ewa Szczurek, Martin Vingron, Jerzy Tiuryn (2012), The
R Package bgmm: Mixture Modeling with Uncertain Knowledge, Journal of
Statistical Software <doi:10.18637/jss.v047.i03>.

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
