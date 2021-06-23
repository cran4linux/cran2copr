%global __brp_check_rpaths %{nil}
%global packname  noisySBM
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Noisy Stochastic Block Mode: Graph Inference by Multiple Testing

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-parallel 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RColorBrewer 

%description
Variational Expectation-Maximization algorithm to fit the noisy stochastic
block model to an observed dense graph and to perform a node clustering.
Moreover, a graph inference procedure to recover the underlying binary
graph. This procedure comes with a control of the false discovery rate.
The method is described in the article "Powerful graph inference with
false discovery rate control" by T. Rebafka, E. Roquain, F. Villers (2020)
<arXiv:1907.10176>.

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
