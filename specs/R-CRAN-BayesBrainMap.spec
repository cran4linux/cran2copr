%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesBrainMap
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Brain Networks and Connectivity with Population-Derived Priors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fMRItools >= 0.5.3
BuildRequires:    R-CRAN-fMRIscrub >= 0.14.5
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pesel 
BuildRequires:    R-CRAN-SQUAREM 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-fMRItools >= 0.5.3
Requires:         R-CRAN-fMRIscrub >= 0.14.5
Requires:         R-CRAN-abind 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-pesel 
Requires:         R-CRAN-SQUAREM 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements Bayesian brain mapping models, including the prior ICA
(independent components analysis) model proposed in Mejia et al. (2020)
<doi:10.1080/01621459.2019.1679638> and the spatial prior ICA model
proposed in proposed in Mejia et al. (2022)
<doi:10.1080/10618600.2022.2104289>. Both models estimate subject-level
brain as deviations from known population-level networks, which are
estimated using standard ICA algorithms. Both models employ an
expectation-maximization algorithm for estimation of the latent brain
networks and unknown model parameters. Includes direct support for
'CIFTI', 'GIFTI', and 'NIFTI' neuroimaging file formats.

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
