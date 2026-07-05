%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  thamesblock
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Truncated Harmonic Mean Estimator of the Marginal Likelihood for Block Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-label.switching 
Requires:         R-CRAN-mclust 
Requires:         R-stats 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-label.switching 

%description
Implements the truncated harmonic mean estimator (THAMES) and other
estimators of the reciprocal marginal likelihood for block models. This is
done via reciprocal importance sampling, using posterior samples and
unnormalized log posterior values. For further information see Metodiev,
Perrot-Dockès, Fouetilou, Latouche & Raftery (2026).

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
