%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  argminCS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Argmin Inference over a Discrete Candidate Set

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-BSDA 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-LDATS 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-BSDA 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-LDATS 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-withr 

%description
Provides methods to construct frequentist confidence sets with valid
marginal coverage for identifying the population-level argmin or argmax
based on IID data. For instance, given an n by p loss matrix—where n is
the sample size and p is the number of models—the CS.argmin() method
produces a discrete confidence set that contains the model with the
minimal (best) expected risk with desired probability. The argmin.HT()
method helps check if a specific model should be included in such a
confidence set. The main implemented method is proposed by Tianyu Zhang,
Hao Lee and Jing Lei (2024) "Winners with confidence: Discrete argmin
inference with an application to model selection".

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
