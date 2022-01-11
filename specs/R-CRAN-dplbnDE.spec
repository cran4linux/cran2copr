%global __brp_check_rpaths %{nil}
%global packname  dplbnDE
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Discriminative Parameter Learning of Bayesian Networks by Differential Evolution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bnclassify >= 0.4.5
Requires:         R-CRAN-bnclassify >= 0.4.5

%description
Implements Differential Evolution (DE) to train parameters of Bayesian
Networks for optimizing the Conditional Log-Likelihood (Discriminative
Learning) instead of the log-likelihood (Generative Learning). Any given
Bayesian Network structure encodes assumptions about conditional
independencies among the attributes and will result in an error if they do
not hold in the data. Such an error includes the classification dimension.
The main goal of Discriminative learning is to minimize this type of
error. This package provides main variants of differential evolution
described in Price & Storn (1996) <doi:10.1109/ICEC.1996.542711> and
recent ones, described in Tanabe & Fukunaga (2014)
<doi:10.1109/CEC.2014.6900380> and Zhang & Sanderson (2009)
<doi:10.1109/TEVC.2009.2014613> with adaptation mechanism for factor
mutarion and crossover rate.

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
