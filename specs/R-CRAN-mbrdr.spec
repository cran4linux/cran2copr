%global __brp_check_rpaths %{nil}
%global packname  mbrdr
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Based Response Dimension Reduction

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Functions for model-based response dimension reduction. Usual dimension
reduction methods in multivariate regression focus on the reduction of
predictors, not responses.  The response dimension reduction is
theoretically founded in Yoo and Cook (2008)
<doi:10.1016/j.csda.2008.07.029>. Later, three model-based response
dimension reduction approaches are proposed in Yoo (2016)
<doi:10.1080/02331888.2017.1410152> and Yoo (2019)
<doi:10.1016/j.jkss.2019.02.001>. The method by Yoo and Cook (2008) is
based on non-parametric ordinary least squares, but the model-based
approaches are done through maximum likelihood estimation. For two
model-based response dimension reduction methods called principal fitted
response reduction and unstructured principal fitted response reduction,
chi-squared tests are provided for determining the dimension of the
response subspace.

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
