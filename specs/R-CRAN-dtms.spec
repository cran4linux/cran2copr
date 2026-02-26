%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dtms
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete-Time Multistate Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mclogit 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-markovchain 
BuildRequires:    R-methods 
Requires:         R-CRAN-mclogit 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-markovchain 
Requires:         R-methods 

%description
Discrete-time multistate models with a user-friendly workflow. The package
provides tools for processing data, several ways of estimating parametric
and nonparametric multistate models, and an extensive set of Markov chain
methods which use transition probabilities derived from the multistate
model. Some of the implemented methods are described in Schneider et al.
(2024) <doi:10.1080/00324728.2023.2176535>, Dudel (2021)
<doi:10.1177/0049124118782541>, Dudel & Myrskylä (2020)
<doi:10.1186/s12963-020-00217-0>, van den Hout (2017)
<doi:10.1201/9781315374321>.

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
