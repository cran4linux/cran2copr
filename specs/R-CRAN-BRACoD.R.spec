%global packname  BRACoD.R
%global packver   0.0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          BRACoD: Bayesian Regression Analysis of Compositional Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-reticulate 

%description
The goal of this method is to identify associations between bacteria and
an environmental variable in 16S or other compositional data. The
environmental variable is any variable which is measure for each
microbiome sample, for example, a butyrate measurement paired with every
sample in the data. Microbiome data is compositional, meaning that the
total abundance of each sample sums to 1, and this introduces severe
statistical distortions. This method takes a Bayesian approach to
correcting for these statistical distortions, in which the total abundance
is treated as an unknown variable. This package runs the python
implementation using reticulate.

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
