%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simulab
%global packver   0.4.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.10
Release:          1%{?dist}%{?buildtag}
Summary:          Simulates a Wide Variety of Data Shapes, Sizes and Distributions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Generates a wide variety of data, in different shapes, sample sizes,
distributions and parameters. The parameters are either drawn at random or
set in advance, and in both cases they are stored with the data, so they
are known and their recovery can be tested. Generators cover declared
variables with treatment assignment and missing values, correlated and
clustered data, latent profile, latent class, factor and item response
models, longitudinal and multilevel processes, survival times with
competing risks, sequences of states, and static, bipartite, multiplex,
temporal and transition networks. Every generator returns batches of
reproducible data sets for the evaluation of statistical methods, the
testing of models and software, and teaching; simulated transition
networks are native 'tna' models.

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
