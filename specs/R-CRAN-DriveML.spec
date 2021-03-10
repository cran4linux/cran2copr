%global packname  DriveML
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Self-Drive Machine Learning Projects

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sampling >= 2.8
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-mlr >= 2.15.0
BuildRequires:    R-CRAN-rmarkdown >= 1.9
BuildRequires:    R-CRAN-ParamHelpers >= 1.12
BuildRequires:    R-CRAN-data.table >= 1.10.4.3
BuildRequires:    R-CRAN-SmartEDA 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-iml 
Requires:         R-CRAN-sampling >= 2.8
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-mlr >= 2.15.0
Requires:         R-CRAN-rmarkdown >= 1.9
Requires:         R-CRAN-ParamHelpers >= 1.12
Requires:         R-CRAN-data.table >= 1.10.4.3
Requires:         R-CRAN-SmartEDA 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-iml 

%description
Implementing some of the pillars of an automated machine learning pipeline
such as (i) Automated data preparation, (ii) Feature engineering, (iii)
Model building in classification context that includes techniques such as
(a) Regularised regression [1], (b) Logistic regression [2], (c) Random
Forest [3], (d) Decision tree [4] and (e) Extreme Gradient Boosting
(xgboost) [5], and finally, (iv) Model explanation (using lift chart and
partial dependency plots). Accomplishes the above tasks by running the
function instead of writing lengthy R codes. Also provides some additional
features such as generating missing at random (MAR) variables and
automated exploratory data analysis. Moreover, function exports the model
results with the required plots in an HTML vignette report format that
follows the best practices of the industry and the academia. [1] Gonzales
G B and De Saeger (2018) <doi:10.1038/s41598-018-21851-7>, [2] Sperandei S
(2014) <doi:10.11613/BM.2014.003>, [3] Breiman L (2001)
<doi:10.1023/A:1010933404324>, [4] Kingsford C and Salzberg S (2008)
<doi:10.1038/nbt0908-1011>, [5] Chen Tianqi and Guestrin Carlos (2016)
<doi:10.1145/2939672.2939785>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
