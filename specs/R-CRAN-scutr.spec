%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scutr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Balancing Multiclass Datasets for Classification Tasks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-smotefamily 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mclust 
Requires:         R-CRAN-smotefamily 
Requires:         R-parallel 
Requires:         R-CRAN-mclust 

%description
Imbalanced training datasets impede many popular classifiers. To balance
training data, a combination of oversampling minority classes and
undersampling majority classes is useful. This package implements the SCUT
(SMOTE and Cluster-based Undersampling Technique) algorithm as described
in Agrawal et. al. (2015) <doi:10.5220/0005595502260234>. Their paper uses
model-based clustering and synthetic oversampling to balance multiclass
training datasets, although other resampling methods are provided in this
package.

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
