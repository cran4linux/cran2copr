%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  movieROC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing the Decision Rules Underlying Binary Classification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-intrval 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-intrval 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-zoo 

%description
Visualization of decision rules for binary classification and Receiver
Operating Characteristic (ROC) curve estimation under different
generalizations: - making the classification subsets flexible to cover
those scenarios where both extremes of the marker are associated with a
higher risk of being positive, considering two thresholds (gROC curve); -
transforming the marker by a function either defined by the user or
resulting from a logistic regression model (hROC curve); - considering a
linear transformation with some fixed parameters introduced by the user,
dynamic parameters or empirically maximizing TPR for each FPR for a
bivariate marker. Also a quadratic transformation with particular
coefficients or a function fitted by a logistic regression model can be
considered (biROC curve); - considering a linear transformation with some
fixed parameters introduced by the user, dynamic parameters or a function
fitted by a logistic regression model (multiROC curve). The classification
regions behind each point of the ROC curve are displayed in both fixed
graphics (plot.buildROC(), plot.regions() or plot.funregions() function)
or videos (movieROC() function).

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
