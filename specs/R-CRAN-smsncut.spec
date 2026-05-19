%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smsncut
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Diagnostic Cutoff Selection under Scale Mixtures of Skew-Normal Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1
BuildRequires:    R-CRAN-sn >= 2.0.0
Requires:         R-CRAN-numDeriv >= 2016.8.1
Requires:         R-CRAN-sn >= 2.0.0

%description
Implements a parametric decision-theoretic framework for optimal
diagnostic cutoff selection under the family of scale mixtures of
skew-normal (SMSN) distributions, including the skew-normal (SN) and
skew-t (ST) models as special cases. The optimal cutoff is defined by
minimising a weighted misclassification risk that incorporates disease
prevalence and asymmetric costs, leading to a likelihood-ratio equation
that generalises the Youden criterion. Under a monotone likelihood ratio
condition, existence, uniqueness, and global optimality of the cutoff are
established. Asymptotic normality and a closed-form plug-in variance
estimator are provided via the implicit function theorem and the
multivariate delta method. Tools for model fitting, cutoff estimation,
confidence intervals, the local identifiability diagnostic, and Monte
Carlo simulation are included. The methodology is described in de Paula,
Mouriño, and Dias Domingues (2026) <doi:10.48550/arXiv.2605.07829>.

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
