%global __brp_check_rpaths %{nil}
%global packname  citrus
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Customer Intelligence Tool for Rapid Understandable Segmentation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-clustMixType >= 0.1.16
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-treeClust 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-CRAN-rpart.utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-clustMixType >= 0.1.16
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-treeClust 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rpart.plot 
Requires:         R-CRAN-rpart.utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 

%description
A tool to easily run and visualise supervised and unsupervised state of
the art customer segmentation. It is built like a pipeline covering the 3
main steps in a segmentation project: pre-processing, modelling, and
plotting. Users can either run the pipeline as a whole, or choose to run
any one of the three individual steps. It is equipped with a supervised
option (tree optimisation) and an unsupervised option (k-clustering) as
default models.

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
