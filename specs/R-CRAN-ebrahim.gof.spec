%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ebrahim.gof
%global packver   2.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit and Calibration Tests for Logistic Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-parallel 
Requires:         R-stats 

%description
Provides a unified battery of goodness-of-fit and calibration tests for
binary logistic regression, runnable in a single call via 'run.all.gof()'.
Around twenty-five tests spanning five decades of literature are
aggregated and grouped by the departure each is built to detect: global
and standardized statistics, partition tests, directed and covariate-space
tests, smoothing and resampling tests, and calibration tests. Each is
obtained from its own package where installed and attributed to its
authors. The package also implements the author's own procedures for
sparse data, where the Hosmer-Lemeshow test loses power: the omnibus
Ebrahim-Farrington test, the directed 'EDGE' test, 'DeepGOF-1' (a
pretrained convolutional statistic whose level comes from the analyst's
own parametric bootstrap rather than from the network), a
Cauchy-combination ensemble, 'legoft()' (a pretrained combination whose
weights are fixed offline and ship frozen, so two analysts obtain the same
p-value), and 'shrink.gof()' for penalized (ridge) logistic regression,
where shrinkage biases the fitted probabilities and invalidates the usual
chi-squared references. For more details see Hosmer (1980)
<doi:10.1080/03610928008827941> and Farrington (1996)
<doi:10.1111/j.2517-6161.1996.tb02086.x>.

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
