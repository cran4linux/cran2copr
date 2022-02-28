%global __brp_check_rpaths %{nil}
%global packname  PoPdesign
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Posterior Predictive (PoP) Design for Phase I Clinical Trials

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magick 
Requires:         R-CRAN-Iso 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magick 

%description
The primary goal of phase I clinical trials is to find the maximum
tolerated dose (MTD). To reach this objective, we introduce a new design
for phase I clinical trials, the posterior predictive (PoP) design. The
PoP design is an innovative model-assisted design that is as simply as the
conventional algorithmic designs as its decision rules can be
pre-tabulated prior to the onset of trial, but is of more flexibility of
selecting diverse target toxicity rates and cohort sizes. The PoP design
has desirable properties, such as coherence and consistency. Moreover, the
PoP design provides better empirical performance than the BOIN and
Keyboard design with respect to high average probabilities of choosing the
MTD and slightly lower risk of treating patients at subtherapeutic or
overly toxic doses.

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
