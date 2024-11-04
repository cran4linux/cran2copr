%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ConfMatrix
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Confusion Matrix

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
Thematic quality indices are provided to facilitate the evaluation and
quality control of geospatial data products (e.g. thematic maps, remote
sensing classifications, etc.). The indices offered are based on the
so-called confusion matrix. This matrix is constructed by comparing the
assigned classes or attributes of a set of pairs of positions or objects
in the product and the ground truth. In this package it is considered that
the classes of the ground truth correspond to the columns and that the
classes of the product to be valued correspond to the rows. The package
offers two object classes with their methods: 'ConfMatrix' (Confusion
matrix) and 'QCCS' (Quality Control Columns Set). The 'ConfMatrix' class
of objects offers more than 20 methods based on the confusion matrix. The
'QCCS' class of objects offers a different perspective in which the ground
truth is considered to allow the values of the column marginals to be
fixed, see Ariza López et al. (2019) <doi:10.3390/app9204240> and Canran
Liu et al. (2007) <doi:10.1016/j.rse.2006.10.010> for more details. The
package was created with 'R6'.

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
