%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Surrogate
%global packver   3.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluation of Surrogate Endpoints in Clinical Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-logistf 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-rvinecopulib 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-MBESS 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-logistf 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-rvinecopulib 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-MBESS 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-tibble 

%description
In a clinical trial, it frequently occurs that the most credible outcome
to evaluate the effectiveness of a new therapy (the true endpoint) is
difficult to measure. In such a situation, it can be an effective strategy
to replace the true endpoint by a (bio)marker that is easier to measure
and that allows for a prediction of the treatment effect on the true
endpoint (a surrogate endpoint). The package 'Surrogate' allows for an
evaluation of the appropriateness of a candidate surrogate endpoint based
on the meta-analytic, information-theoretic, and causal-inference
frameworks. Part of this software has been developed using funding
provided from the European Union's Seventh Framework Programme for
research, technological development and demonstration (Grant Agreement no
602552), the Special Research Fund (BOF) of Hasselt University
(BOF-number: BOF2OCPO3), GlaxoSmithKline Biologicals, Baekeland Mandaat
(HBC.2022.0145), and Johnson & Johnson Innovative Medicine.

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
