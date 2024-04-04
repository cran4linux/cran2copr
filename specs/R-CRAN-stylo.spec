%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stylo
%global packver   0.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          Stylometric Multivariate Analyses

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-pamr 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-tsne 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-pamr 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-class 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-tsne 

%description
Supervised and unsupervised multivariate methods, supplemented by GUI and
some visualizations, to perform various analyses in the field of
computational stylistics, authorship attribution, etc. For further
reference, see Eder et al. (2016),
<https://journal.r-project.org/archive/2016/RJ-2016-007/index.html>. You
are also encouraged to visit the Computational Stylistics Group's website
<https://computationalstylistics.github.io/>, where a reasonable amount of
information about the package and related projects are provided.

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
