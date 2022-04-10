%global __brp_check_rpaths %{nil}
%global packname  gensvm
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          A Generalized Multiclass Support Vector Machine

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
The GenSVM classifier is a generalized multiclass support vector machine
(SVM). This classifier aims to find decision boundaries that separate the
classes with as wide a margin as possible. In GenSVM, the loss function is
very flexible in the way that misclassifications are penalized.  This
allows the user to tune the classifier to the dataset at hand and
potentially obtain higher classification accuracy than alternative
multiclass SVMs.  Moreover, this flexibility means that GenSVM has a
number of other multiclass SVMs as special cases. One of the other
advantages of GenSVM is that it is trained in the primal space, allowing
the use of warm starts during optimization.  This means that for common
tasks such as cross validation or repeated model fitting, GenSVM can be
trained very quickly. Based on: G.J.J. van den Burg and P.J.F. Groenen
(2018) <https://www.jmlr.org/papers/v17/14-526.html>.

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
