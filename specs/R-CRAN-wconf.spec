%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wconf
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted Confusion Matrix

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Allows users to create weighted confusion matrices and accuracy metrics
that help with the model selection process for classification problems,
where distance from the correct category is important. The package
includes several weighting schemes which can be parameterized, as well as
custom configuration options. Furthermore, users can decide whether they
wish to positively or negatively affect the accuracy score as a result of
applying weights to the confusion matrix. 'wconf' integrates well with the
'caret' package, but it can also work standalone when provided data in
matrix form. References: Kuhn, M. (2008) "Building Perspective Models in R
Using the caret Package" <doi:10.18637/jss.v028.i05> Monahov, A. (2021)
"Model Evaluation with Weighted Threshold Optimization (and the mewto R
package)" <doi:10.2139/ssrn.3805911> Van de Velden, M., Iodice D'Enza, A.,
Markos, A., Cavicchia, C. (2023) "A general framework for implementing
distances for categorical variables" <arXiv:2301.02190v1>.

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
