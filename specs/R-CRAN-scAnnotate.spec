%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scAnnotate
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          An Automated Cell Type Annotation Tool for Single-Cell RNA-Sequencing Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Seurat >= 4.0.5
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MTPS 
BuildRequires:    R-CRAN-harmony 
Requires:         R-CRAN-Seurat >= 4.0.5
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-CRAN-MTPS 
Requires:         R-CRAN-harmony 

%description
An entirely data-driven cell type annotation tools, which requires
training data to learn the classifier, but not biological knowledge to
make subjective decisions. It consists of three steps: preprocessing
training and test data, model fitting on training data, and cell
classification on test data. See Xiangling Ji,Danielle Tsao, Kailun Bai,
Min Tsao, Li Xing, Xuekui Zhang.(2022)<doi:10.1101/2022.02.19.481159> for
more details.

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
