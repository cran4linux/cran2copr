%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  daltoolboxdp
%global packver   1.2.727
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.727
Release:          1%{?dist}%{?buildtag}
Summary:          Python-Based Extensions for Data Analytics Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tspredit 
BuildRequires:    R-CRAN-daltoolbox 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-FSelector 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-smotefamily 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-stats 
Requires:         R-CRAN-tspredit 
Requires:         R-CRAN-daltoolbox 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-FSelector 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-smotefamily 
Requires:         R-CRAN-reticulate 
Requires:         R-stats 

%description
Provides Python-based extensions to enhance data analytics workflows,
particularly for tasks involving data preprocessing and predictive
modeling. Includes tools for data sampling, transformation, feature
selection, balancing strategies (e.g., SMOTE), and model construction.
These capabilities leverage Python libraries via the reticulate interface,
enabling seamless integration with a broader machine learning ecosystem.
Supports instance selection and hybrid workflows that combine R and Python
functionalities for flexible and reproducible analytical pipelines. The
architecture is inspired by the Experiment Lines approach, which promotes
modularity, extensibility, and interoperability across tools. More
information on Experiment Lines is available in Ogasawara et al. (2009)
<doi:10.1007/978-3-642-02279-1_20>.

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
