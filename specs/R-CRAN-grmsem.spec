%global __brp_check_rpaths %{nil}
%global packname  grmsem
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Genetic-Relationship-Matrix Structural Equation Modelling (GRMSEM)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-msm >= 1.6
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-optimParallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-msm >= 1.6
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-optimParallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Quantitative genetics tool supporting the modelling of multivariate
genetic variance structures in quantitative data. It allows fitting
different models through multivariate genetic-relationship-matrix (GRM)
structural equation modelling (SEM) in unrelated individuals, using a
maximum likelihood approach. Specifically, it combines genome-wide
genotyping information, as captured by GRMs, with twin-research-based SEM
techniques, St Pourcain et al. (2017)
<doi:10.1016/j.biopsych.2017.09.020>, Shapland et al. (2020)
<doi:10.1101/2020.08.14.251199>.

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
