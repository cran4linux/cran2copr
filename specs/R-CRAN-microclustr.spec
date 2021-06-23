%global __brp_check_rpaths %{nil}
%global packname  microclustr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Entity Resolution with Random Partition Priors for Microclustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-stats 

%description
An implementation of the model in Betancourt, Zanella, Steorts (2020)
<arXiv:2004.02008>, which performs microclustering models for categorical
data. The package provides a vignette for two proposed methods in the
paper as well as two standard Bayesian non-parametric clustering
approaches for entity resolution. The experiments are reproducible and
illustrated using a simple vignette. LICENSE: GPL-3 + file license.

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
