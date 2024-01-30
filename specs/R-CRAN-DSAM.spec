%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DSAM
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Data Splitting Algorithms for Model Developments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-kohonen 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-kohonen 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pROC 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-xgboost 

%description
Providing six different algorithms that can be used to split the available
data into training, test and validation subsets with similar distribution
for hydrological model developments. The dataSplit() function will help
you divide the data according to specific requirements, and you can refer
to the par.default() function to set the parameters for data splitting.
The getAUC() function will help you measure the similarity of distribution
features between the data subsets. For more information about the data
splitting algorithms, please refer to: Chen et al. (2022)
<doi:10.1016/j.jhydrol.2022.128340>, Zheng et al. (2022)
<doi:10.1029/2021WR031818>.

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
