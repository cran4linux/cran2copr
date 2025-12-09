%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easybgm
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extracting and Visualizing Bayesian Graphical Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bgms >= 0.1.4
BuildRequires:    R-CRAN-BDgraph 
BuildRequires:    R-CRAN-BGGM 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-bgms >= 0.1.4
Requires:         R-CRAN-BDgraph 
Requires:         R-CRAN-BGGM 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-coda 

%description
Fit and visualize the results of a Bayesian analysis of networks commonly
found in psychology. The package supports fitting cross-sectional network
models fitted using the packages 'BDgraph', 'bgms' and 'BGGM', as well as
network comparison fitted using the 'bgms' and 'BBGM'. The package
provides the parameter estimates, posterior inclusion probabilities,
inclusion Bayes factor, and the posterior density of the parameters. In
addition, for 'BDgraph' and 'bgms' it allows to assess the posterior
structure space. Furthermore, the package comes with an extensive suite
for visualizing results.

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
