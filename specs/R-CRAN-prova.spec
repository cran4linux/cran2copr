%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prova
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Probabilistic-Statistical Variate Analysis with Automated Markov-Chain Monte Carlo

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-parallel 
Requires:         R-CRAN-extraDistr 
Requires:         R-parallel 

%description
Calculate posterior joint and conditional probabilities, probability
distributions of population frequencies, and information-theoretic
measures, by means of Bayesian nonparametric methods. Data imputation is
automatic and done in a principled way. Markov-chain Monte Carlo
calculations are automatically handled and do not require user
supervision. Applications range from statistical estimation and
probabilistic hypothesis testing to evidence-based inference and decision
making, in a wide range of disciplines from astrophysics to medicine. For
more details and examples see for instance Porta Mana et al. (2026)
<doi:10.31219/osf.io/8nr56>, Dunson & Bhattacharya (2011)
<doi:10.1093/acprof:oso/9780199694587.003.0005>, Lindley & Novick (1981)
<doi:10.1214/aos/1176345331>, Bernardo & Smith (2000)
<doi:10.1002/9780470316870>, Müller et al. (2015)
<doi:10.1007/978-3-319-18968-0>. Requires the packages 'Nimble',
'parallel', 'extraDistr'.

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
