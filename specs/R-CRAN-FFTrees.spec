%global __brp_check_rpaths %{nil}
%global packname  FFTrees
%global packver   1.6.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Generate, Visualise, and Evaluate Fast-and-Frugal Decision Trees

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-rpart 
Requires:         R-graphics 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyselect 

%description
Create, visualize, and test fast-and-frugal decision trees (FFTs) using
methods described in Phillips, Neth, Woike & Gaissmaier. (2017). FFTs are
very simple decision trees for binary classification problems. FFTs can be
preferable to more complex algorithms because they are easy to
communicate, require very little information, and are robust against
overfitting.

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
