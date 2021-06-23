%global __brp_check_rpaths %{nil}
%global packname  localIV
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}%{?buildtag}
Summary:          Estimation of Marginal Treatment Effects using LocalInstrumental Variables

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-KernSmooth >= 2.5.0
BuildRequires:    R-mgcv >= 1.8.19
BuildRequires:    R-CRAN-sampleSelection >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 0.4.4
BuildRequires:    R-stats 
Requires:         R-KernSmooth >= 2.5.0
Requires:         R-mgcv >= 1.8.19
Requires:         R-CRAN-sampleSelection >= 1.2.0
Requires:         R-CRAN-rlang >= 0.4.4
Requires:         R-stats 

%description
In the generalized Roy model, the marginal treatment effect (MTE) can be
used as a building block for constructing conventional causal parameters
such as the average treatment effect (ATE) and the average treatment
effect on the treated (ATT). Given a treatment selection equation and an
outcome equation, the function mte() estimates the MTE via the
semiparametric local instrumental variables method or the normal selection
model. The function mte_at() evaluates MTE at different values of the
latent resistance u with a given X = x, and the function mte_tilde_at()
evaluates MTE projected onto the estimated propensity score. The function
ace() estimates population-level average causal effects such as ATE, ATT,
or the marginal policy relevant treatment effect.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
