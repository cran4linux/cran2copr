%global __brp_check_rpaths %{nil}
%global packname  LongituRF
%global packver   0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Random Forests for Longitudinal Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-latex2exp 
Requires:         R-stats 
Requires:         R-CRAN-randomForest 
Requires:         R-rpart 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-latex2exp 

%description
Random forests are a statistical learning method widely used in many areas
of scientific research essentially for its ability to learn complex
relationships between input and output variables and also its capacity to
handle high-dimensional data. However, current random forests approaches
are not flexible enough to handle longitudinal data.  In this package, we
propose a general approach of random forests for high-dimensional
longitudinal data. It includes a flexible stochastic model which allows
the covariance structure to vary over time. Furthermore, we introduce a
new method which takes intra-individual covariance into consideration to
build random forests. The method is fully detailled in Capitaine et.al.
(2020) <doi:10.1177/0962280220946080> Random forests for high-dimensional
longitudinal data.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
